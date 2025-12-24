const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// In-memory storage for game states
const games = {};

// API Routes

// Create a new game
app.post('/api/games', (req, res) => {
    const { gameId, gameState } = req.body;
    
    if (!gameId || !gameState) {
        return res.status(400).json({ error: 'Game ID and state are required' });
    }
    
    games[gameId] = gameState;
    console.log(`Game ${gameId} created`);
    res.json({ success: true, gameId });
});

// Get game state
app.get('/api/games/:gameId', (req, res) => {
    const { gameId } = req.params;
    
    if (!games[gameId]) {
        return res.status(404).json({ error: 'Game not found' });
    }
    
    res.json(games[gameId]);
});

// Update game state
app.put('/api/games/:gameId', (req, res) => {
    const { gameId } = req.params;
    const { gameState } = req.body;
    
    if (!games[gameId]) {
        return res.status(404).json({ error: 'Game not found' });
    }
    
    if (!gameState) {
        return res.status(400).json({ error: 'Game state is required' });
    }
    
    games[gameId] = gameState;
    console.log(`Game ${gameId} updated`);
    res.json({ success: true });
});

// Delete game (optional - for cleanup)
app.delete('/api/games/:gameId', (req, res) => {
    const { gameId } = req.params;
    
    if (games[gameId]) {
        delete games[gameId];
        console.log(`Game ${gameId} deleted`);
        res.json({ success: true });
    } else {
        res.status(404).json({ error: 'Game not found' });
    }
});

// Health check
app.get('/api/health', (req, res) => {
    res.json({ status: 'ok', gamesCount: Object.keys(games).length });
});

// Serve manifest.json with correct MIME type and cache control
app.get('/manifest.json', (req, res) => {
    res.setHeader('Content-Type', 'application/manifest+json');
    res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
    res.setHeader('Pragma', 'no-cache');
    res.setHeader('Expires', '0');
    res.sendFile(path.join(__dirname, 'manifest.json'));
});

// Serve static files from root directory
app.use(express.static(__dirname, {
    extensions: ['html', 'htm']
}));

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on http://localhost:${PORT}`);
    console.log(`Game API available at http://localhost:${PORT}/api`);
});
