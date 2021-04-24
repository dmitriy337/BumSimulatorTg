using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace BumSimulatorApi.Models
{
    public class AppContext: DbContext
    {

        public DbSet<Tg_user> Tg_users { get; set; }
        public DbSet<BumWork> BumWorks { get; set; }
        public DbSet<Character> Characters { get; set; }
        public DbSet<Food> Foods { get; set; }
        public DbSet<Health> Healths { get; set; }
        public DbSet<House> Houses { get; set; }
        public DbSet<Learning> Learnings { get; set; }
        public DbSet<NormalWork> NormalWorks { get; set; }


        public AppContext()
        {

            Database.EnsureCreated();
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            string AppConnectionString = Config.ConnectionTobString;

            optionsBuilder.UseNpgsql(AppConnectionString);
        }
    }
}
