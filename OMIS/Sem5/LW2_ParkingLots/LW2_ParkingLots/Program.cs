using LW2_ParkingLots.Components;
using LW2_ParkingLots.Components.Account;
using LW2_ParkingLots.Model.Persistence;
using LW2_ParkingLots.Model.Persistence.Repositories;
using LW2_ParkingLots.Model.Services;
using Microsoft.AspNetCore.Components.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

builder.Services.AddCascadingAuthenticationState();
builder.Services.AddScoped<IdentityUserAccessor>();
builder.Services.AddScoped<IdentityRedirectManager>();
builder.Services.AddScoped<AuthenticationStateProvider, IdentityRevalidatingAuthenticationStateProvider>();

builder.Services.AddAuthentication(options =>
    {
        options.DefaultScheme = IdentityConstants.ApplicationScheme;
        options.DefaultSignInScheme = IdentityConstants.ExternalScheme;
    })
    .AddIdentityCookies();

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection") ?? throw new InvalidOperationException("Connection string 'DefaultConnection' not found.");
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(connectionString));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();

builder.Services.AddIdentityCore<ApplicationUser>(options => options.SignIn.RequireConfirmedAccount = true)
    .AddEntityFrameworkStores<ApplicationDbContext>()
    .AddSignInManager()
    .AddDefaultTokenProviders();

builder.Services.AddSingleton<IEmailSender<ApplicationUser>, IdentityNoOpEmailSender>();

// Domain model services
builder.Services.AddTransient<IParkingLotRepository, ParkingLotRepository>();
builder.Services.AddTransient<IZoneRepository, ZoneRepository>();
builder.Services.AddTransient<IPaymentRepository, PaymentRepository>();
builder.Services.AddTransient<IReviewRepository, ReviewRepository>();
builder.Services.AddTransient<IProfileRepository, ProfileRepository>();
builder.Services.AddTransient<ILoginRepository, LoginRepository>();
builder.Services.AddTransient<IRegisterRepository, RegisterRepository>();

builder.Services.AddTransient<IParkingLotService, ParkingLotService>();
builder.Services.AddTransient<IZoneService, ZoneService>();
builder.Services.AddTransient<IPaymentService, PaymentService>();
builder.Services.AddTransient<IReviewService, ReviewService>();
builder.Services.AddTransient<IProfileService, ProfileService>();
builder.Services.AddTransient<ILoginService, LoginService>();
builder.Services.AddTransient<IRegisterService, RegisterService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseMigrationsEndPoint();
}
else
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

// Add additional endpoints required by the Identity /Account Razor components.
app.MapAdditionalIdentityEndpoints();

app.Run();
