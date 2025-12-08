# Quick Start Guide

## Setup (One-time)

1. **Install Node.js** (if not already installed)
   - Download from: https://nodejs.org/
   - Version 14 or higher recommended

2. **Install dependencies**
   ```bash
   npm install
   ```

## Running the Server

1. **Start the server**
   ```bash
   npm start
   ```

2. **Access the game**
   - Open browser: `http://localhost:3000/BloodOnTheClocktowerApp/Blood_On_The_Clocktower_Farsi_Online.html`

## Testing on Multiple Devices

### Option 1: Same Network (Local Testing)

1. Find your computer's IP address:
   - **Windows**: Open Command Prompt, type `ipconfig`, look for "IPv4 Address"
   - **Mac/Linux**: Open Terminal, type `ifconfig` or `ip addr`, look for your network interface IP

2. On other devices (phones, tablets, other computers):
   - Connect to the same Wi-Fi network
   - Open browser and go to: `http://YOUR_IP_ADDRESS:3000/BloodOnTheClocktowerApp/Blood_On_The_Clocktower_Farsi_Online.html`
   - Example: `http://192.168.1.100:3000/BloodOnTheClocktowerApp/Blood_On_The_Clocktower_Farsi_Online.html`

### Option 2: Deploy to Cloud

Deploy to services like:
- **Heroku**: `heroku create` then `git push heroku main`
- **Railway**: Connect GitHub repo
- **Render**: Connect GitHub repo
- **DigitalOcean**: Use App Platform

After deployment, update the `API_BASE_URL` in the HTML file to your server URL.

## How to Play

1. **One person creates the game:**
   - Enter your name
   - Click "ایجاد بازی جدید" (Create New Game)
   - Set number of players and enter all player names
   - Click "شروع بازی" (Start Game)
   - Share the Game ID with other players

2. **Other players join:**
   - Enter the Game ID
   - Enter your name (must match one of the names entered by creator)
   - Click "پیوستن به بازی" (Join Game)

3. **Gameplay:**
   - Each player sees only their own role
   - During night phase, each player sees only their own action when it's their turn
   - During day phase, all players see the same public information

## Troubleshooting

- **"Game not found"**: Make sure the server is running and all devices are using the same server URL
- **Can't connect from other devices**: Check firewall settings, make sure port 3000 is open
- **Game state not updating**: Check browser console for errors, verify server is running

