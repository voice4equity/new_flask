# Flask Setup

## Development Setup

```bash
# Activate virtual environment
pyenv activate new_flask

# Install dependencies (if you deleted requirements.txt)
# pip install -r requirements.txt

# Start Tailwind watcher (in a separate terminal)
npm run dev

# Run development server
flask run
```

## Database Setup

This project supports both SQLite (default) and PostgreSQL.

### Using SQLite (default)
No additional setup required. The database will be created at `instance/app.db` when you run:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Using PostgreSQL
1. Install and start PostgreSQL on your system
2. Create a database: `createdb new_flask`
3. Update the `.env` file:
   ```
   DB_TYPE=postgres
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=new_flask
   ```
4. Run migrations:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Testing
```bash
pytest
```

## Deployment
For production, remember to:
1. Set a strong `SECRET_KEY` in the `.env` file
2. Set `FLASK_DEBUG=0` in the `.env` file
3. Use a proper database (PostgreSQL or SQLite work great)
4. Build the CSS for production: `npm run build`

