using SkiaSharp;

namespace LW4
{
    public partial class MainPage : ContentPage
    {
        private SKBitmap? _bitmap;
        private readonly MainPageViewmodel viewmodel;

        public MainPage(MainPageViewmodel vm)
        {
            InitializeComponent();

            BindingContext = vm;
            viewmodel = vm;

            Task.Run(async () =>
            {
                using Stream stream = await FileSystem.OpenAppPackageFileAsync("colors.png");

                _bitmap = SKBitmap.Decode(stream);
            });
        }

        private void SKCanvasView_PaintSurface(object sender, SkiaSharp.Views.Maui.SKPaintSurfaceEventArgs args)
        {
            SKImageInfo info = args.Info;
            SKSurface surface = args.Surface;
            SKCanvas canvas = surface.Canvas;
            canvas.Clear();

            if (_bitmap is null)
            {
                return;
            }

            float scale = Math.Min((float)info.Width / _bitmap.Width,
                                   (float)info.Height / _bitmap.Height);
            float x = (info.Width - scale * _bitmap.Width) / 2;
            float y = (info.Height - scale * _bitmap.Height) / 2;
            SKRect destRect = new(x, y, x + scale * _bitmap.Width,
            y + scale * _bitmap.Height);

            canvas.DrawBitmap(_bitmap, destRect);
        }

        private void Button_Pressed(object sender, EventArgs e)
        {
            var kmeans = new KMeans(_bitmap!, viewmodel.ClusterCount, viewmodel.Iterations);

            var x = kmeans.GetClusterCenters();
        }
    }

}
