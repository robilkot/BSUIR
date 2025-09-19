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

            builder.Services.AddControllers();

            builder.Services.AddDbContext<IndexDbContext>(options =>
                options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));

            builder.Services.AddScoped<IndexRepository>();
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
