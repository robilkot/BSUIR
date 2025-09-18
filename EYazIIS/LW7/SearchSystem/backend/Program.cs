using backend.DatetimeProviders;
using backend.Model;
using backend.Repository;
using Microsoft.EntityFrameworkCore;

namespace backend
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            builder.Services.AddControllers();

            builder.Services.AddDbContext<IndexDbContext>(options =>
                options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));

            builder.Services.AddScoped<IIndexRepository, IndexRepository>();
            builder.Services.AddTransient<IDatetimeProvider, DatetimeProvider>();

            var app = builder.Build();

            using var scope = app.Services.CreateScope();
            var services = scope.ServiceProvider;                
            var indexRepository = services.GetRequiredService<IIndexRepository>();
            var datetimeProvider = services.GetRequiredService<IDatetimeProvider>();

            var crawler = new Crawler(app.Configuration, indexRepository, datetimeProvider);

            // todo not await, but bg stuff
            crawler.IndexAll();

            app.Run();
            
            // Configure the HTTP request pipeline.

            app.UseHttpsRedirection();

            app.UseAuthorization();


            app.MapControllers();

            app.Run();
        }
    }
}
