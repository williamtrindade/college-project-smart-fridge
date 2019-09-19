# Config Laravel
### Download PHP Packages
 * Run `composer install`.

### Create SQLite Database
 * Create a file called `database.sqlite`, and reference in .env file, `DB_CONNECTION=sqlite`.
 * Run this command `sudo apt-get install php7.3-sqlite3` to install sqlite in php.
 * Run the migrations with this command `php artisan migrate`.

 ### Build the frontend
 * Run `npm install` and `npm run dev`.

 ### Run the seeds
  * `php artisan db:seed`