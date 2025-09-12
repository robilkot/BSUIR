using backend.Model;
using Microsoft.EntityFrameworkCore;
using System.Threading.Tasks;

namespace backend
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.

            builder.Services.AddControllers();

            builder.Services.AddDbContext<IndexDbContext>(options =>
                options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

            builder.Services.AddScoped<IIndexRepository, IndexRepository>();
            builder.Services.AddTransient<IDatetimeProvider, DatetimeProvider>();

            var app = builder.Build();


            using (var scope = app.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                
                var indexRepository = services.GetRequiredService<IIndexRepository>();
                var datetimeProvider = services.GetRequiredService<IDatetimeProvider>();

                var crawler = new Crawler(app.Configuration, indexRepository, datetimeProvider);

                await crawler.IndexAll();                
            }

            app.Run();
            
            // Configure the HTTP request pipeline.

            app.UseHttpsRedirection();

            app.UseAuthorization();


            app.MapControllers();

            app.Run();
        }
    }
}
