import bpy
import bmesh
from mathutils import Vector


class RemoveHiddenPolygonsOperator(bpy.types.Operator):
    bl_idname = "mesh.remove_hidden_polygons"
    bl_label = "Удалить невидимые полигоны"
    bl_description = "Удаляет полигоны, невидимые относительно активной камеры"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        camera = context.scene.camera
        obj = context.active_object

        if not camera or not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "Необходимо выбрать объект и установить активную камеру")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='OBJECT')
        mesh = obj.data

        projection_matrix = camera.calc_matrix_camera(
            bpy.context.evaluated_depsgraph_get(),
            x=bpy.context.scene.render.resolution_x,
            y=bpy.context.scene.render.resolution_y,
            scale_x=bpy.context.scene.render.pixel_aspect_x,
            scale_y=bpy.context.scene.render.pixel_aspect_y,
        )

        for poly in mesh.polygons:
            verts_world = [obj.matrix_world @ mesh.vertices[v].co for v in poly.vertices]
            not_in_frustum = self.not_in_frustum(verts_world, camera, projection_matrix)
            occluded = self.is_occluded(poly, obj, camera)

            if not_in_frustum or occluded:
                poly.hide = True
            else:
                poly.hide = False

        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}

    # Проверяет, находятся ли все вершины полигона вне пределов обзора камеры
    def not_in_frustum(self, verts, camera, projection_matrix):
        all_not_in_frustum: bool = True

        for vert in verts:
            vert_camera_space = camera.matrix_world.inverted() @ vert

            # Преобразуем координаты камеры в нормализованные координаты экрана
            vert_ndc = projection_matrix @ vert_camera_space.to_4d()

            # Если w < 0, вершина находится за камерой
            if vert_ndc.w < 0:
                continue

            # Нормализуем
            vert_ndc /= vert_ndc.w

            # Проверяем, находятся ли координаты в пределах [-1, 1] по x, y, z
            if not (-1 <= vert_ndc.x <= 1 and -1 <= vert_ndc.y <= 1 and -1 <= vert_ndc.z <= 1):
                continue

            # В поле зрения, значит False
            all_not_in_frustum = False

        return all_not_in_frustum

    # Проверяет, перекрыт ли полигон другими полигонами с помощью трассировки лучей
    def is_occluded(self, polygon, obj, camera):
        scene = bpy.context.scene
        depsgraph = bpy.context.evaluated_depsgraph_get()
        bm = bmesh.new()
        bm.from_mesh(obj.data)

        cam_origin = camera.location
        poly_center = sum((obj.matrix_world @ obj.data.vertices[v].co for v in polygon.vertices), Vector()) / len(polygon.vertices)
        direction = (poly_center - cam_origin).normalized()

        result, location, normal, index, hit_obj, _ = scene.ray_cast(depsgraph, cam_origin, direction)

        bm.free()

        if result and hit_obj == obj:
            return (location - cam_origin).length < (poly_center - cam_origin).length - 0.01  # Запас, чтобы избежать погрешности
        return False


def menu_func(self, context):
    self.layout.operator(RemoveHiddenPolygonsOperator.bl_idname)


def register():
    bpy.utils.register_class(RemoveHiddenPolygonsOperator)
    bpy.types.VIEW3D_MT_edit_mesh.append(menu_func)


def unregister():
    bpy.utils.unregister_class(RemoveHiddenPolygonsOperator)
    bpy.types.VIEW3D_MT_edit_mesh.remove(menu_func)


if __name__ == "__main__":
    register()
