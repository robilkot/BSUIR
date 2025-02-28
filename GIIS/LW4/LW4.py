import bpy
import bmesh
from math import radians, cos, sin


class AffineTransformationsPanel(bpy.types.Panel):
    bl_label = "Affine Transformations"
    bl_idname = "PT_AffineTransformations"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Affine'

    def draw(self, context):
        layout = self.layout
        props = context.scene.affine_props

        layout.prop(props, "transformation_type", text="Type")

        if props.transformation_type == 'TRANSLATE':
            layout.prop(props, "translate_vector")
        elif props.transformation_type == 'ROTATE':
            layout.prop(props, "rotate_axis")
            layout.prop(props, "rotate_angle")
        elif props.transformation_type == 'SCALE':
            layout.prop(props, "scale_vector")
        elif props.transformation_type == 'REFLECT':
            layout.prop(props, "reflect_axis")
        elif props.transformation_type == 'PERSPECTIVE':
            layout.prop(props, "perspective_factors")

        layout.operator("object.apply_affine_transformation")


# Transformation logic
def translate(vertices, vector):
    return [[v[0] + vector[0], v[1] + vector[1], v[2] + vector[2], 1] for v in vertices]


def scale(vertices, factors):
    return [[v[0] * factors[0], v[1] * factors[1], v[2] * factors[2], 1] for v in vertices]


def rotate(vertices, axis, angle):
    angle = radians(angle)
    cos_, sin_ = cos(angle), sin(angle)
    x, y, z = axis
    norm = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    x, y, z = x / norm, y / norm, z / norm

    rotation_matrix = [
        [cos_ + (1 - cos_) * x ** 2, (1 - cos_) * x * y - sin_ * z, (1 - cos_) * x * z + sin_ * y, 0],
        [(1 - cos_) * y * x + sin_ * z, cos_ + (1 - cos_) * y ** 2, (1 - cos_) * y * z - sin_ * x, 0],
        [(1 - cos_) * z * x - sin_ * y, (1 - cos_) * z * y + sin_ * x, cos_ + (1 - cos_) * z ** 2, 0],
        [0, 0, 0, 1]
    ]
    return [[sum(a * b for a, b in zip(row, v)) for row in rotation_matrix] for v in vertices]


def reflect(vertices, axis):
    reflect_matrix = {
        'X': [[-1, 0, 0, 0],
              [ 0, 1, 0, 0],
              [ 0, 0, 1, 0],
              [ 0, 0, 0, 1]],
        'Y': [[1,  0, 0, 0],
              [0, -1, 0, 0],
              [0,  0, 1, 0],
              [0,  0, 0, 1]],
        'Z': [[1, 0,  0, 0],
              [0, 1,  0, 0],
              [0, 0, -1, 0],
              [0, 0,  0, 1]]
    }
    return [[sum(a * b for a, b in zip(row, v)) for row in reflect_matrix[axis]] for v in vertices]


def perspective(vertices, factors):
    px, py, pz = factors
    persp_matrix = [[1, 0, 0, px],
                    [0, 1, 0, py],
                    [0, 0, 1, pz],
                    [0, 0, 0, 1]]
    return [[sum(a * b for a, b in zip(row, v)) for row in persp_matrix] for v in vertices]


# Executor
class ApplyAffineTransformation(bpy.types.Operator):
    bl_idname = "object.apply_affine_transformation"
    bl_label = "Apply"

    def execute(self, context):
        props = context.scene.affine_props
        obj = context.object
        if obj is None or obj.type != 'MESH':
            self.report({'WARNING'}, "No active mesh object selected")
            return {'CANCELLED'}

        bm = bmesh.new()
        bm.from_mesh(obj.data)

        vertices = [list(v.co) + [1] for v in bm.verts]

        if props.transformation_type == 'TRANSLATE':
            vertices = translate(vertices, props.translate_vector)
        elif props.transformation_type == 'ROTATE':
            vertices = rotate(vertices, props.rotate_axis, props.rotate_angle)
        elif props.transformation_type == 'SCALE':
            vertices = scale(vertices, props.scale_vector)
        elif props.transformation_type == 'REFLECT':
            vertices = reflect(vertices, props.reflect_axis)
        elif props.transformation_type == 'PERSPECTIVE':
            vertices = perspective(vertices, props.perspective_factors)

        for v, new_co in zip(bm.verts, vertices):
            v.co = new_co[:3]

        bm.to_mesh(obj.data)
        bm.free()
        obj.data.update()
        return {'FINISHED'}


class AffineProperties(bpy.types.PropertyGroup):
    transformation_type: bpy.props.EnumProperty(
        items=[
            ('TRANSLATE', "Translate", "Move object"),
            ('ROTATE', "Rotate", "Rotate object"),
            ('SCALE', "Scale", "Scale object"),
            ('REFLECT', "Reflect", "Reflect across an axis"),
            ('PERSPECTIVE', "Perspective", "Apply perspective transformation")
        ],
        default='TRANSLATE'
    )
    translate_vector: bpy.props.FloatVectorProperty(name="Shift", default=(0.0, 0.0, 0.0))
    rotate_axis: bpy.props.FloatVectorProperty(name="Axis", default=(0.0, 0.0, 1.0), subtype='XYZ')
    rotate_angle: bpy.props.FloatProperty(name="Angle", default=0.0)
    scale_vector: bpy.props.FloatVectorProperty(name="Factor", default=(1.0, 1.0, 1.0))
    reflect_axis: bpy.props.EnumProperty(
        items=[('X', "X", "Reflect across X-axis"),
               ('Y', "Y", "Reflect across Y-axis"),
               ('Z', "Z", "Reflect across Z-axis")],
        default='X'
    )
    perspective_factors: bpy.props.FloatVectorProperty(name="Factor", default=(0.0, 0.0, 0.0))


classes = [AffineTransformationsPanel, ApplyAffineTransformation, AffineProperties]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.affine_props = bpy.props.PointerProperty(type=AffineProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.affine_props


if __name__ == "__main__":
    register()
