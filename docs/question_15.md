Question 15: Django Database Migrations

Django database migrations are the process of synchronizing the database schema with changes made to Django models, ensuring that the database structure reflects the current state of the application's data model. Here's how to perform Django database migrations with a server-based relational database like SQLite:
Steps for Performing Django Database Migrations:

    Make Model Changes: Modify your Django models (models.py) to reflect the desired changes, such as adding new fields, altering existing fields, or creating new models.

    Generate Migrations: Run the following command in the terminal to generate migration files based on the model changes:

    bash

python manage.py makemigrations

Review Migration Files: Review the generated migration files (located in the migrations directory within each app) to ensure they reflect the intended changes.

Apply Migrations: Apply the migrations to the database by running the following command:

bash

    python manage.py migrate

    Verify Changes: Verify that the database schema reflects the changes made to the models by inspecting the database tables or using Django admin interface.

    Optional: Rollback Migrations: If needed, rollback migrations to a previous state using the migrate command with the --fake option followed by the migration name or zero to revert all migrations.

By following these steps, you can effectively manage database migrations in a Django project using a server-based relational database like SQLite.