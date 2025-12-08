# Blood on the Clocktower - Online Server Setup

This server enables multi-device gameplay for the Blood on the Clocktower online version.

## Setup Instructions

### 1. Install Dependencies

```bash
npm install
```

### 2. Start the Server

```bash
npm start
```

Or for development with auto-reload:

```bash
npm run dev
```

The server will start on `http://localhost:3000`

### 3. Access the Game

Open your browser and navigate to:
```
http://localhost:3000/BloodOnTheClocktowerApp/Blood_On_The_Clocktower_Farsi_Online.html
```

Or if you have the file structure set up, the server will serve files from the root directory.

## API Endpoints

- `POST /api/games` - Create a new game
- `GET /api/games/:gameId` - Get game state
- `PUT /api/games/:gameId` - Update game state
- `DELETE /api/games/:gameId` - Delete a game
- `GET /api/health` - Health check

## Deployment

### Local Network Testing

To test on multiple devices on your local network:

1. Find your computer's local IP address:
   - Windows: `ipconfig` (look for IPv4 Address)
   - Mac/Linux: `ifconfig` or `ip addr`

2. Update the `API_BASE_URL` in the HTML file to use your IP:
   ```javascript
   var API_BASE_URL = 'http://YOUR_IP_ADDRESS:3000';
   ```

3. Make sure all devices are on the same network

4. Access the game from other devices using:
   ```
   http://YOUR_IP_ADDRESS:3000/BloodOnTheClocktowerApp/Blood_On_The_Clocktower_Farsi_Online.html
   ```

### Production Deployment

For production, deploy to services like:
- Heroku
- Railway
- Render
- DigitalOcean
- AWS
- Any Node.js hosting service

Update the `API_BASE_URL` in the HTML file to point to your deployed server URL.

## Notes

- Game state is stored in memory (will be lost on server restart)
- For persistent storage, consider adding a database (MongoDB, PostgreSQL, etc.)
- The server uses CORS to allow cross-origin requests

