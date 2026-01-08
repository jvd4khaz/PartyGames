# The Thing - Simplified Card Game Version

## Overview

This is a simplified version of The Thing board game that can be played with a standard deck of playing cards and a companion app (or paper tracking sheets). The game maintains the core hidden role, paranoia, and base management mechanics while reducing complexity.

## Components Needed

### Physical Components
- 1 standard deck of playing cards (52 cards)
- 1 joker (optional, for special events)
- Paper and pen for tracking (or use companion app)
- 4-8 players

### Companion App Functions (or Paper Tracking)
- Track suspicion levels for each player
- Track base status (Fuel, Food, Damage)
- Track weather conditions
- Track rescue helicopter progress
- Randomize contagion checks
- Manage hidden role information

## Setup

### 1. Role Distribution
- Shuffle the deck
- Deal 1 card face down to each player (this is their secret role)
- **Red cards (Hearts/Diamonds) = Human**
- **Black cards (Spades/Clubs) = Alien**
- For 4-5 players: 1 Alien
- For 6-7 players: 1-2 Aliens (randomly determine)
- For 8 players: 2 Aliens
- Players look at their card but keep it secret

### 2. Base Status (Track in app or on paper)
- **Fuel**: Start at 10 (4-5 players), 12 (6 players), 14 (7-8 players)
- **Food**: Start at 8 (4-5 players), 10 (6 players), 12 (7-8 players)
- **Damage**: Start at 0
- **Rescue Helicopter**: Start at position 0 (not called yet)

### 3. Player Setup
- Each player starts with **Suspicion Level 0** (tracked in app)
- Each player draws **2 Action Cards** (see Action Cards section)
- Shuffle remaining cards to form the Action Deck

### 4. Action Cards
Create Action Cards from the deck:
- **USE cards**: Ace, 2, 3, 4, 5 of any suit (20 cards total)
- **REPAIR cards**: 6, 7, 8 of any suit (12 cards total)
- **SABOTAGE cards**: 9, 10 of any suit (8 cards total)
- **JACK = Blood Test** (4 cards)
- **QUEEN = Fire Test** (4 cards)
- **KING = Special Item** (4 cards - see Items section)

Shuffle all Action Cards together to form the Action Deck.

## Gameplay

The game is played in rounds. Each round consists of 6 phases:

### Phase 1: Weather Conditions
- Roll a die or use app to determine weather:
  - **1-2**: Clear (no fuel consumption)
  - **3-4**: Storm (consume 2 Fuel)
  - **5-6**: Blizzard (consume 3 Fuel, advance Freezing Track if Boiler damaged)

### Phase 2: Base Maintenance
- Consume Fuel based on weather
- If not enough Fuel, add Damage (1 Damage per missing Fuel)
- If Damage reaches 5, the base is destroyed (Aliens win if Humans don't escape)
- If Boiler is damaged (Damage ≥ 3), advance Freezing Track
- If Freezing Track reaches maximum, Humans freeze (Aliens win)

### Phase 3: Draw Cards
- Each player draws Action Cards to reach hand size of 3
- If deck runs out, shuffle discard pile

### Phase 4: Action Phase
Players take turns (starting with Leader) to:

**Option A: Play an Action Card**
- Choose a location (see Locations section)
- Play 1 Action Card face down to Leader
- Move your character to that location
- Leader collects all face-down cards

**Option B: Rest (Dormitory)**
- Discard all cards in hand
- Draw 3 new cards from deck
- Skip this round's actions

**After all players have acted:**
- Leader shuffles all played Action Cards
- Leader reveals and assigns cards one at a time
- Each card must be assigned to a player in an appropriate location
- Resolve actions (see Action Resolution)

### Phase 5: Encounters
If 2+ players are in the same location, an **Encounter** occurs:

1. **Contagion Check**: Each player secretly draws 1 card from the deck
   - If you draw a **Black card**: You are infected (become Alien)
   - If you draw a **Red card**: You remain Human
   - Return the card to deck and shuffle
   - **Important**: If you're already an Alien, you can choose to show a Red card to bluff

2. **Suspicion**: Each player in the encounter increases their Suspicion by 1

3. **If Alien is Exposed**: If an Alien has been revealed (through Test), resolve combat:
   - Compare Alien Strength vs. Number of Humans in location
   - If Alien wins: Assimilate 1 player or sabotage location
   - If Humans win: Alien flees

### Phase 6: Tests and Accusations
- Players with **JACK (Blood Test)** can test the most suspicious player
- Players with **QUEEN (Fire Test)** can test any player
- Tested player reveals their role card
- If Human: Move suspicion to 0 (proven innocent)
- If Alien: Alien is exposed, game enters combat phase

### Phase 7: Food Consumption
- Consume 2 Food tokens
- If not enough Food: All players reduce hand size to 2 (discard 1 card)

### Phase 8: Leader Change
- Pass leadership to next player
- Advance Rescue Helicopter if S.O.S. was sent (see Radio Room)

## Locations (Simplified)

Players choose locations verbally. Track locations on paper or in app.

### 1. **Generator Room** (Power)
- USE: Add 1 Fuel
- REPAIR: Remove 1 Damage
- SABOTAGE: Add 1 Damage
- If 2+ Damage: Power failure (Darkness rules apply)

### 2. **Boiler Room** (Heat)
- USE: Add 1 Fuel
- REPAIR: Remove 1 Damage
- SABOTAGE: Add 1 Damage
- If 3+ Damage: Freezing begins

### 3. **Kitchen** (Food)
- USE: Add 2 Food
- SABOTAGE: Remove 2 Food

### 4. **Radio Room** (Rescue)
- USE: Send S.O.S. (start Rescue Helicopter track)
- REPAIR: Remove 1 Damage
- SABOTAGE: Add 1 Damage
- Must be fully repaired (0 Damage) to send S.O.S.

### 5. **Armory** (Weapons)
- USE: Draw 2 cards, keep 1 (if KING, you get a weapon)
- SABOTAGE: Remove 1 weapon card from game

### 6. **Laboratory** (Tests)
- USE: Draw 1 test token (use app to randomize Blood Bag vs. Failure)
- SABOTAGE: Remove 1 test token

### 7. **Warehouse** (Items)
- USE: Draw 1 item card (KING = special item)
- SABOTAGE: Remove 1 item card

### 8. **Leisure Room** (Safe Zone)
- No actions available
- Players return here after actions
- Can trade items/weapons here

### 9. **Base Helicopter** (Escape Route 1)
- USE: Add 1 Fuel to helicopter (needs 3 Fuel total)
- REPAIR: Remove 1 Damage
- SABOTAGE: Add 1 Damage
- Escape: If 0 Damage and 3+ Fuel, Humans can escape

### 10. **Shed/Snow Cat** (Escape Route 2)
- USE: Add 1 Fuel to Snow Cat (needs 2 Fuel total)
- REPAIR: Remove 1 Damage
- SABOTAGE: Add 1 Damage
- Escape: If 0 Damage and 2+ Fuel, Humans can escape

## Action Resolution

When Leader assigns Action Cards:

1. **USE**: Player performs location's USE action
2. **REPAIR**: Player removes 1 Damage from location
3. **SABOTAGE**: Player adds 1 Damage to location OR performs location's sabotage action

**Cooperation Bonus**: If 2+ players are in same location when USE/REPAIR is assigned, action is performed twice (but only 1 player is laid down)

## Items and Weapons (KING cards)

When you draw a KING, you get a special ability:

- **Spades KING**: Firearm (avoid 1 encounter)
- **Hearts KING**: Flashlight (ignore Darkness)
- **Diamonds KING**: Keys (needed for escape)
- **Clubs KING**: Flamethrower (fight Alien, 3 uses)

## Winning Conditions

### Humans Win If:
- All Humans escape via Rescue Helicopter/Base Helicopter/Snow Cat with NO Aliens
- All Aliens are eliminated AND Humans escape

### Aliens Win If:
- Alien escapes with Humans (hidden or exposed)
- Alien escapes alone
- All Humans are assimilated
- Base is destroyed (Damage ≥ 5) and Humans don't escape
- Freezing Track reaches maximum

## Escape Sequence

When escape is attempted:

1. **Rescue Helicopter**: 
   - Must have been called (S.O.S. sent)
   - Helicopter must have arrived (tracked in app)
   - Least suspicious player boards first
   - Each subsequent player needs approval from all on board
   - When helicopter leaves, reveal all roles
   - If any Alien on board, Aliens win
   - If all Humans on board, Humans win

2. **Base Helicopter/Snow Cat**:
   - Must be fully repaired and fueled
   - Player with Keys starts escape
   - Same boarding process as Rescue Helicopter

## Companion App Features

The app should track:

1. **Player Status**:
   - Suspicion level (0-5)
   - Role (Human/Alien) - hidden until tested
   - Hand size
   - Items/weapons owned

2. **Base Status**:
   - Fuel count
   - Food count
   - Damage count
   - Freezing track position
   - Power failure status

3. **Rescue Status**:
   - S.O.S. sent (yes/no)
   - Helicopter position (0-10)
   - Helicopter fuel

4. **Randomization**:
   - Weather die roll
   - Contagion checks (draw random card result)
   - Test results (Blood Bag vs. Failure)

5. **Location Tracking**:
   - Which players are in which locations
   - Location damage status

## Simplified Rules for First Play

For your first game, use these even simpler rules:

1. **Skip Weather**: Always consume 1 Fuel per round
2. **Skip Freezing Track**: Only track Damage
3. **Skip Items**: Ignore KING card special abilities
4. **Simple Tests**: Only use JACK for Blood Tests
5. **Fixed Locations**: Use only 5 locations: Generator, Boiler, Kitchen, Radio, Leisure Room

## Tips for Play

- Use the app for all tracking to reduce bookkeeping
- Keep role cards hidden at all times
- When infected, secretly switch your role card
- Bluffing is key - even as Alien, you want to appear helpful
- Work together to repair base, but watch for saboteurs
- Don't reveal your role unless tested or escaping

## Card Reference

- **A-5**: USE (20 cards)
- **6-8**: REPAIR (12 cards)
- **9-10**: SABOTAGE (8 cards)
- **JACK**: Blood Test (4 cards)
- **QUEEN**: Fire Test (4 cards)
- **KING**: Special Item (4 cards)
- **Role Cards**: Red = Human, Black = Alien

---

This simplified version maintains the core paranoia and hidden role mechanics while being playable with just a deck of cards and basic tracking (paper or app).



