# Wiki

**Wiki** is a simple, Wikipedia-like online encyclopedia built using Python and Django as part of the CS50W curriculum. This project allows users to view, search, edit, and create pages using Markdown syntax, which are then dynamically converted to HTML for display.

## Features

- **Home Page**: Lists all encyclopedia entries alphabetically, with clickable links to each page.
- **Entry Pages**: Each entry is its own webpage, displaying the content written in Markdown.
- **Search**: Allows users to search for entries by title. If the search term matches an entry exactly, the user is redirected to that entry’s page. If there are partial matches, a list of relevant entries is shown.
- **New Page Creation**: Users can create new entries with Markdown-formatted content, provided that an entry with the same title doesn’t already exist.
- **Edit Page**: Users can edit existing entries, with the current Markdown content pre-populated in an editable text area.
- **Random Page**: A button that redirects users to a randomly selected entry.

## Files

### `encyclopedia/`

- **`urls.py`**: Defines URL patterns for the main application, routing requests to corresponding views.
- **`views.py`**: Contains all the view functions for displaying entries, handling search, and rendering the New and Edit pages.
- **`util.py`**: Helper functions to read, save, and list entries stored as Markdown files.
- **`models.py`**: Although not required for this project, this file could be used to define models if the app is expanded in the future.

### `templates/encyclopedia/`

- **`layout.html`**: Base template containing the layout structure and navigation bar, extended by all other templates.
- **`index.html`**: Template for the home page, displaying the list of available entries.
- **`entry.html`**: Template for displaying a single entry’s content.
- **`new_page.html`**: Template for the page where users can create new entries.
- **`edit_page.html`**: Template for editing an existing entry.
- **`search.html`**: Template for displaying search results.

### `static/encyclopedia/`

- **CSS**: Custom styling for the application, making the app visually appealing and responsive.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd wiki
   ```

2. **Install dependencies**:
   Ensure you have Django installed. If not, install it via pip:
   ```bash
   pip install django
   ```

3. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   Open your browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

1. **View Entries**: On the home page, click any entry title to view its content.
2. **Search**: Use the search bar to find an entry by title. If there's an exact match, you’ll be redirected to that entry; otherwise, a list of potential matches will appear.
3. **Create New Entry**: Click on “Create New Page” in the navigation bar to create a new entry. Fill in the title and content in Markdown format, then click “Save.”
4. **Edit Existing Entry**: While viewing an entry, click on “Edit” to modify its content. The edit form will pre-fill with the entry’s Markdown text.
5. **Random Page**: Click the “Random Page” link to view a randomly selected entry.

## Markdown Formatting

Pages are written using Markdown, which allows for easy text formatting. Some Markdown examples:
- `# Heading` for large headers.
- `**bold**` for bold text.
- `[Link Text](URL)` for hyperlinks.

## Future Enhancements

- **User Authentication**: Add login functionality to restrict editing to authorized users.
- **Database Integration**: Store entries in a database for more efficient retrieval and management.
- **Image Embedding**: Enable image support in Markdown.

## Acknowledgments

This project is part of the CS50W course, where foundational code was provided to guide the development of the application. Special thanks to the CS50 staff for their support and resources.
