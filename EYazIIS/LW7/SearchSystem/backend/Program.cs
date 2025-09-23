using backend.DatetimeProviders;
using backend.Model;
using backend.Repository;
using backend.Services;
using Microsoft.EntityFrameworkCore;

namespace backend
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            builder.Services.AddLogging(builder =>
            {
                builder.AddFilter("System.Net.Http.HttpClient", LogLevel.Warning);
            });

            builder.Services.AddControllers();

            builder.Services.AddDbContext<IndexDbContext>(options =>
                options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));

            builder.Services.AddTransient<IndexRepository>();
            builder.Services.AddScoped<NLPService>();
            builder.Services.AddTransient<IDatetimeProvider, DatetimeProvider>();
            builder.Services.AddHostedService<Crawler>();

            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen();

            builder.Services.AddHttpClient<NLPService>(client =>
            {
                client.BaseAddress = new Uri("http://localhost:8000/");
                client.Timeout = TimeSpan.FromSeconds(10);
            });

            var app = builder.Build();

            using (var scope = app.Services.CreateScope())
            {
                using (var dbContext = scope.ServiceProvider.GetRequiredService<IndexDbContext>())
                {
                    dbContext.Database.EnsureCreated();
                }
            }

            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }


            app.UseHttpsRedirection();

            app.UseAuthorization();

            app.MapControllers();

            app.Run();
        }
    }
}
