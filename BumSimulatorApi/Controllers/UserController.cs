using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace BumSimulatorApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UserController : ControllerBase
    {

        Models.AppContext db;
        public UserController(Models.AppContext context)
        {
            db = context;

        }

        [HttpGet("userId={id}")]
        public async Task<ActionResult<IEnumerable<Models.Tg_user>>> Get(int id)
        {
            Models.Tg_user user = await db.Tg_users.Include(x => x.character).FirstOrDefaultAsync(x => x.Id == id);

            if (user == null)
                return NotFound();
            return new ObjectResult(user);
        }

        [HttpDelete("userId={id}")]
        public async Task<ActionResult<IEnumerable<Models.Tg_user>>> Delete(int id)
        {
            Models.Tg_user user = db.Tg_users.Include(x => x.character).FirstOrDefault(x => x.Id == id);
            if (user == null)
            {
                return NotFound();
            }
            if (user.character != null)
            {
                db.Characters.Remove(user.character);
            }
            db.Tg_users.Remove(user);
            await db.SaveChangesAsync();
            return Ok(user);
        }



        [HttpPost("userd={id}&username={username}&firstname={firstname}&lastname={lastname}")]
        public async Task<ActionResult<Models.Tg_user>> Post(long userId, string username, string firstname, string lastname)
        {
            if (userId.ToString()==null ^ username == null)
            {
                return BadRequest();
            }

            Models.Tg_user user = new Models.Tg_user
            {
                Id = userId,
                Username = firstname,
                FirstName = firstname,
                LastName = lastname
            };

            db.Tg_users.Add(user);
            await db.SaveChangesAsync();
            return Ok(user);
        }

    }
}
