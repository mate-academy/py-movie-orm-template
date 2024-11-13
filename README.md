# Project: Movie Mate ORM Template

This project provides a Django ORM setup to manage and analyze a movie database, with models representing movies, genres, certifications, directors, and stars. The setup also includes management commands for populating and cleaning the database after migrations.

## Project Structure

The following directory structure organizes the Django application:

```
.
├── README.md
├── db
│   ├── __init__.py
│   ├── management
│   │   └── commands
│   │       ├── clean_movies.py      # Command to clean the database
│   │       └── populate_movies.py   # Command to populate the database
│   ├── migrations                   # Django migrations
│   └── models.py                    # Model definitions
├── dto                               # Data Transfer Objects for processing data
│   └── movie.py
├── files
│   └── movies.csv                    # CSV file with movie data for import
├── init_django_orm.py                # Django ORM initialization
├── manage.py                         # Django management commands
├── requirements.txt                  # Project dependencies
├── services                          # Utility services
│   ├── clean_db.py                   # Utility to clean the database
│   ├── csv_mapper.py                 # Service for parsing CSV files
│   └── db_importer.py                # Service for importing data into the database
└── settings.py                       # Project settings
```

## Models Overview

### Base Model: `StaffMovie`

**StaffMovie** is an abstract base class for genres, certifications, directors, and stars. It includes common fields:
- `name` (CharField): The name of the entity (unique).
- `slug` (AutoSlugField): A slug generated from the `name`.
- `description` (TextField): Optional description.
- `poster` (URLField): Optional URL for an associated image.

### `Genre`, `Certification`, `Director`, `Star`

These models inherit from **StaffMovie** and represent various static attributes or entities related to movies:
- **Genre**: Categories like Drama, Comedy, etc.
- **Certification**: Ratings such as G, PG, or R.
- **Director**: Individuals who directed the movie.
- **Star**: Actors or actresses who starred in the movie.

### `Movie`

Represents a movie in the database with fields:
- `name` (CharField): The movie title.
- `year` (IntegerField): Year of release, validated between 1888 and two years from the current year.
- `time` (IntegerField): Duration in minutes, valid between 1 and 600.
- `imdb` (FloatField): IMDb rating, valid between 0 and 10.
- `votes` (IntegerField): Number of votes, limited to 10 million.
- `meta_score` (FloatField): Optional Metascore rating, valid between 0 and 100.
- `gross` (FloatField): Optional gross earnings, capped at 1 billion.
- `description` (TextField): Synopsis or description of the movie.
- `price` (DecimalField): Optional price of the movie, up to 999.99.

#### Relationships
- `certification`: A foreign key to **Certification**.
- `genres`: Many-to-many relationship with **Genre** via **MovieGenre**.
- `directors`: Many-to-many relationship with **Director** via **MovieDirector**.
- `stars`: Many-to-many relationship with **Star** via **MovieStar**.

### Through Models for Many-to-Many Relationships

#### `MovieGenre`

Intermediate table for `Movie` and `Genre`:
- `importance_level` (IntegerField): Importance of the genre in the movie context (from 1 - Very Low to 5 - Very High).
- `added_date` (DateField): Date the genre was assigned.
- `notes` (TextField): Additional notes.

#### `MovieDirector`

Intermediate table for `Movie` and `Director`:
- `role` (CharField): The director's role (e.g., Main Director, Assistant Director).
- `collaboration_years` (IntegerField): Number of years the director has worked with the movie crew.
- `comments` (TextField): Additional comments.

#### `MovieStar`

Intermediate table for `Movie` and `Star`:
- `role` (CharField): The star's role type (Lead, Supporting, Cameo).
- `screen_time` (IntegerField): Screen time in minutes.
- `salary` (DecimalField): Salary paid for the role.
- `character_name` (CharField): The name of the character portrayed.
- `debut` (BooleanField): Whether it was the actor's debut movie.

## Setup Instructions

1. **Clone the Repository**:
   Begin by cloning the repository to your local machine.
   ```bash
   git clone https://github.com/wspjoy2011/movie-mate-orm-template.git
   cd movie-mate-orm-template
   ```

2. **Create and Activate a Virtual Environment**:
   It’s recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required dependencies listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   Run migrations to create tables in the database.
   ```bash
   python manage.py migrate
   ```

5. **Populate or Clean the Database**:
   - **Populate**: To load initial data from the `movies.csv` file, use:
     ```bash
     python manage.py populate_movies
     ```
   - **Clean**: To remove all movie data:
     ```bash
     python manage.py clean_movies
     ```

## Additional Information

### Database Diagram

You can view the database schema and relationships via [this link](https://dbdiagram.io/d/MoviesTemplate-6733b977e9daa85aca38436d).

## Example Use Cases

The project supports common queries, including filtering movies by genre, certification, director, and star roles, as well as querying aggregate values like average IMDb rating or gross earnings.