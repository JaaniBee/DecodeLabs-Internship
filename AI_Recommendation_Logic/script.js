// Built-in dataset of movies
const MOVIES_DATA = [
    { id: 1, title: "The Matrix", genres: ["Action", "Sci-Fi"] },
    { id: 2, title: "Inception", genres: ["Action", "Adventure", "Sci-Fi", "Thriller"] },
    { id: 3, title: "The Dark Knight", genres: ["Action", "Crime", "Drama", "Thriller"] },
    { id: 4, title: "Pulp Fiction", genres: ["Crime", "Drama"] },
    { id: 5, title: "Forrest Gump", genres: ["Drama", "Romance"] },
    { id: 6, title: "The Shawshank Redemption", genres: ["Drama"] },
    { id: 7, title: "The Avengers", genres: ["Action", "Adventure", "Sci-Fi"] },
    { id: 8, title: "Titanic", genres: ["Drama", "Romance"] },
    { id: 9, title: "Toy Story", genres: ["Animation", "Adventure", "Comedy", "Family"] },
    { id: 10, title: "The Lion King", genres: ["Animation", "Adventure", "Drama", "Family"] },
    { id: 11, title: "Spirited Away", genres: ["Animation", "Adventure", "Family", "Fantasy"] },
    { id: 12, title: "Interstellar", genres: ["Adventure", "Drama", "Sci-Fi"] },
    { id: 13, title: "Gladiator", genres: ["Action", "Adventure", "Drama"] },
    { id: 14, title: "Jurassic Park", genres: ["Action", "Adventure", "Sci-Fi", "Thriller"] },
    { id: 15, title: "The Silence of the Lambs", genres: ["Crime", "Drama", "Thriller"] },
    { id: 16, title: "Superbad", genres: ["Comedy"] },
    { id: 17, title: "The Hangover", genres: ["Comedy"] },
    { id: 18, title: "Knives Out", genres: ["Comedy", "Crime", "Drama", "Mystery"] },
    { id: 19, title: "Mad Max: Fury Road", genres: ["Action", "Adventure", "Sci-Fi"] },
    { id: 20, title: "La La Land", genres: ["Comedy", "Drama", "Music", "Romance"] },
];

let selectedGenres = new Set();

// Extract all unique genres
function getAllGenres() {
    const genresSet = new Set();
    MOVIES_DATA.forEach(movie => {
        movie.genres.forEach(genre => genresSet.add(genre));
    });
    return Array.from(genresSet).sort();
}

// Calculate Jaccard Similarity
function calculateJaccardSimilarity(userGenres, movieGenres) {
    const set1 = new Set(userGenres);
    const set2 = new Set(movieGenres);
    
    let intersection = 0;
    for (let item of set1) {
        if (set2.has(item)) {
            intersection++;
        }
    }
    
    const union = new Set([...set1, ...set2]).size;
    
    if (union === 0) return 0;
    return intersection / union;
}

// Recommend Movies
function recommendMovies() {
    const userGenresArr = Array.from(selectedGenres);
    
    if (userGenresArr.length === 0) {
        return [];
    }

    const scoredMovies = [];
    
    MOVIES_DATA.forEach(movie => {
        const score = calculateJaccardSimilarity(userGenresArr, movie.genres);
        if (score > 0) {
            scoredMovies.push({ movie, score });
        }
    });

    // Sort descending by score, then alphabetically
    scoredMovies.sort((a, b) => {
        if (b.score !== a.score) {
            return b.score - a.score;
        }
        return a.movie.title.localeCompare(b.movie.title);
    });

    return scoredMovies.slice(0, 5);
}

// UI Rendering
function renderGenres() {
    const container = document.getElementById('genre-container');
    const genres = getAllGenres();
    
    genres.forEach(genre => {
        const pill = document.createElement('div');
        pill.className = 'genre-pill';
        pill.textContent = genre;
        
        pill.addEventListener('click', () => {
            if (selectedGenres.has(genre)) {
                selectedGenres.delete(genre);
                pill.classList.remove('active');
            } else {
                selectedGenres.add(genre);
                pill.classList.add('active');
            }
            updateRecommendations();
        });
        
        container.appendChild(pill);
    });
}

function updateRecommendations() {
    const container = document.getElementById('results-container');
    container.innerHTML = ''; // Clear current
    
    if (selectedGenres.size === 0) {
        container.innerHTML = '<div class="placeholder">Select genres to see recommendations!</div>';
        return;
    }
    
    const recommendations = recommendMovies();
    
    if (recommendations.length === 0) {
        container.innerHTML = '<div class="placeholder">No movies found matching all selected genres. Try different combinations!</div>';
        return;
    }
    
    recommendations.forEach((rec, index) => {
        const matchPercent = Math.round(rec.score * 100);
        
        const card = document.createElement('div');
        card.className = 'movie-card';
        // Add a slight delay for staggered animation
        card.style.animationDelay = `${index * 0.1}s`;
        
        card.innerHTML = `
            <div class="movie-title">${rec.movie.title}</div>
            <div class="movie-genres">${rec.movie.genres.join(', ')}</div>
            <div class="movie-match">${matchPercent}% Match</div>
        `;
        
        container.appendChild(card);
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderGenres();
});
