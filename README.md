# Wellness Tracker

## Setup

```bash
# Clone the repository
git clone https://github.com/tarakguptadrebes/wellness_tracker.git
cd wellness_tracker

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Run Project

```bash
# Run migrations
python manage.py migrate

#Launch the app
python manage.py runserver
```