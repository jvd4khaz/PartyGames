Blood on the Clocktower
Complete Rules Reference for App Development

Blood on the Clocktower is a social deduction game where players are divided into two teams: the good team (Townsfolk and Outsiders) and the evil team (Minions and Demon). The game is moderated by a Storyteller who manages the flow of information and ensures rules are followed. This document provides comprehensive rules for developing an app that acts as the Storyteller.

## Game Overview

**Players:** 5-20 players (5-15 standard, 16-20 with Travellers)

**Objective:**
- **Good Team:** Execute the Demon to win
- **Evil Team:** Keep the Demon alive until only two players remain

**Key Features:**
- Dead players can still participate in discussions and vote once
- Open communication is allowed at all times
- The Storyteller has significant discretion in managing information
- Each character has unique abilities that activate during specific phases

## Game Editions

### Trouble Brewing (Beginner Edition)
The recommended starting edition. Features the Imp as the Demon and focuses on information gathering and deduction.

### Bad Moon Rising (Advanced Edition)
More lethal edition with Demons that can kill multiple players. Requires closer teamwork and strategic sacrifice.

### Sects & Violets (Chaos Edition)
Features characters that can switch sides and change roles. Players may not know which Demon is in play initially.

### Travellers & Fabled (Expansion)
Cannot be played alone. Adds Traveller characters (known roles, hidden alignment) and Fabled characters (Storyteller-controlled balancing mechanisms).

## Setup

### Physical Setup
1. Arrange chairs in a circle or square facing each other
2. Ensure the Storyteller can easily move between players
3. Place the Town Square board in the center with life tokens for each player
4. Place vote tokens in the center of the board

### Character Distribution
The number of each character type depends on player count:

**5 Players:**
- 3 Townsfolk
- 0 Outsiders
- 1 Minion
- 1 Demon

**6 Players:**
- 3 Townsfolk
- 1 Outsider
- 1 Minion
- 1 Demon

**7 Players:**
- 5 Townsfolk
- 0 Outsiders
- 1 Minion
- 1 Demon

**8 Players:**
- 5 Townsfolk
- 1 Outsider
- 1 Minion
- 1 Demon

**9 Players:**
- 5 Townsfolk
- 2 Outsiders
- 1 Minion
- 1 Demon

**10 Players:**
- 7 Townsfolk
- 0 Outsiders
- 1 Minion
- 1 Demon

**11 Players:**
- 7 Townsfolk
- 1 Outsider
- 1 Minion
- 1 Demon

**12 Players:**
- 7 Townsfolk
- 2 Outsiders
- 1 Minion
- 1 Demon

**13 Players:**
- 9 Townsfolk
- 0 Outsiders
- 1 Minion
- 1 Demon

**14 Players:**
- 9 Townsfolk
- 1 Outsider
- 1 Minion
- 1 Demon

**15 Players:**
- 9 Townsfolk
- 2 Outsiders
- 1 Minion
- 1 Demon

**16-20 Players:**
- Use standard 15-player setup
- Additional players become Travellers

### Character Assignment Process
1. Storyteller secretly selects character tokens according to the distribution chart
2. Shuffle and randomly distribute tokens to players
3. Players secretly look at their character and remember their role
4. Players return tokens to the Storyteller
5. Storyteller arranges tokens in the Grimoire matching seating order

## Game Phases

### Night Phase

All players close their eyes. The Storyteller wakes characters in a specific order to perform their abilities. The order varies by edition, but generally follows this pattern for Trouble Brewing:

**Night Order (Trouble Brewing):**
1. **Washerwoman** - Learn one of two players is a specific Townsfolk
2. **Librarian** - Learn one of two players is a specific Outsider
3. **Investigator** - Learn one of two players is a specific Minion
4. **Chef** - Learn how many pairs of evil players are sitting next to each other
5. **Empath** - Learn how many evil players are sitting next to you
6. **Fortune Teller** - Learn if a player is the Demon or not (may get false information)
7. **Undertaker** - Learn which character was executed today (if any)
8. **Monk** - Choose a player to protect from the Demon
9. **Ravenkeeper** - If you die tonight, learn a player's character
10. **Virgin** - If nominated, the nominator is executed instead
11. **Slayer** - Once per game, choose a player; if they are the Demon, they die
12. **Soldier** - You cannot die at night
13. **Mayor** - If only 3 players remain and you die, good wins
14. **Butler** - Each night, choose a player; you must vote how they vote
15. **Drunk** - You think you are a Townsfolk, but you are not
16. **Recluse** - You may register as evil or as a Demon, even if dead
17. **Saint** - If you are executed, evil wins
18. **Poisoner** - Each night, choose a player; their ability malfunctions
19. **Spy** - You appear as good to all abilities; you can see the Grimoire
20. **Scarlet Woman** - If the Demon dies, you become the Demon
21. **Imp** - Each night, choose a player; they die (you are the Demon)

**Storyteller Actions:**
- Wake each character in order
- Use silent signals to communicate
- Record all information given and received
- Manage the Demon's kill selection
- Apply any poisoning or protection effects

### Day Phase

**Discussion Period:**
- Players open their eyes
- Open discussion begins
- Players can share information, make accusations, or strategize
- Private conversations are allowed
- No time limit (Storyteller may impose one if needed)

**Nomination Phase:**
- Any living player can nominate another player for execution
- Nominator states: "I nominate [Player Name]"
- Nominated player may respond
- Other players may discuss
- Voting occurs immediately after discussion

**Voting:**
- All living players vote simultaneously
- Dead players have one vote total for the remainder of the game
- Majority vote required to execute
- If tied or no majority, no execution occurs
- Each player can only nominate once per day

**Execution:**
- Executed player's token is flipped on the Town Square
- Storyteller places a shroud token on their character in the Grimoire
- Character and alignment are NOT revealed
- Executed player becomes dead but can still participate

**End of Day:**
- If Demon is executed, good team wins
- If only 2 players remain alive, evil team wins
- Otherwise, proceed to next Night phase

## Character Roles (Trouble Brewing)

### Townsfolk

**Washerwoman**
- Each night, learn one of two players is a specific Townsfolk
- Storyteller chooses which information to give

**Librarian**
- Each night, learn one of two players is a specific Outsider
- Storyteller chooses which information to give

**Investigator**
- Each night, learn one of two players is a specific Minion
- Storyteller chooses which information to give

**Chef**
- Each night, learn how many pairs of evil players are sitting next to each other
- Counts pairs, not individuals

**Empath**
- Each night, learn how many evil players are sitting next to you (one or both neighbors)
- If you are dead, you learn 0

**Fortune Teller**
- Each night, choose a player; learn if they are the Demon
- You start knowing a good player is the Demon (false information)
- Storyteller may give false information

**Undertaker**
- Each day, if someone was executed yesterday, learn their character
- Only works if someone was executed the previous day

**Monk**
- Each night, choose a player; they cannot die tonight
- Protection lasts until the next day

**Ravenkeeper**
- If you die at night, choose a player; learn their character
- Ability activates only if you die during the night

**Virgin**
- The first time you are nominated, if the nominator is a Townsfolk, they are executed instead
- Only works once per game

**Slayer**
- Once per game, during the day, choose a player; if they are the Demon, they die
- Can be used during any day phase

**Soldier**
- You cannot die at night
- Still vulnerable to execution

**Mayor**
- If only 3 players remain (including you) and you die, good wins instead of evil
- Special win condition override

**Butler**
- Each night, choose a player; tomorrow, you must vote how they vote
- You cannot vote differently from your chosen player

### Outsiders

**Drunk**
- You think you are a Townsfolk, but you are not
- You are actually an Outsider
- Your ability does not work

**Recluse**
- You may register as evil or as a Demon, even if dead
- Storyteller may show you as evil to other abilities
- You are still good

**Saint**
- If you are executed, evil wins
- Good team must avoid executing you

### Minions

**Poisoner**
- Each night, choose a player; their ability malfunctions
- They receive false information or their ability fails
- Effect lasts until the next night

**Spy**
- You appear as good to all abilities
- You can look at the Grimoire
- You know who the Demon is

**Scarlet Woman**
- If the Demon dies, you become the Demon
- Transformation happens immediately
- You keep your Scarlet Woman ability

### Demon

**Imp**
- Each night, choose a player; they die
- You are the Demon
- If you are executed, evil loses

## Storyteller Signals

During the Night phase, the Storyteller uses silent signals:

- **"Open your eyes":** Tap twice on shoulder or knee
- **"Close your eyes":** Cover your own eyes with hand
- **"Yes":** Nod head
- **"No":** Shake head
- **"This player":** Point at player
- **"This is a Good player":** Point at player, then thumbs-up
- **"This is an Evil player":** Point at player, then thumbs-down
- **"0, 1, 2, 3...":** Show that number of fingers (zero = circle with thumb and fingers)
- **"Specific character":** Show character token or point at icon on character sheet

## Key Rules

### Communication Rules
1. **Open Communication:** Players may speak freely at any time, publicly or privately
2. **No Peeking:** Players must not look into the Grimoire or hidden materials
3. **Consult Storyteller:** Players can ask the Storyteller questions for clarification
4. **Respectful Play:** Maintain a kind and respectful environment

### Death Rules
1. **Dead Players:** Can still talk, vote once total, and participate in discussions
2. **Dead Players:** Must still close eyes during Night phase
3. **Dead Players:** Cannot use character abilities (unless ability specifies otherwise)
4. **Character Reveal:** Executed players' characters are NOT revealed

### Voting Rules
1. **Living Players:** Vote on every nomination
2. **Dead Players:** Have one vote total for the remainder of the game
3. **Majority Required:** More than half of living players must vote to execute
4. **One Nomination Per Day:** Each player can only nominate once per day

### Ability Rules
1. **Immediate Activation:** Abilities activate when used
2. **Drunkenness/Poisoning:** Some abilities may malfunction
3. **Storyteller Discretion:** Storyteller has significant control over information given
4. **False Information:** Some characters may receive false information

## Winning Conditions

### Good Team Wins If:
- The Demon is executed
- If multiple Demons exist, all must be executed
- If a Demon is on the good team, they must still be dead for good to win

### Evil Team Wins If:
- Only two players remain alive (the Demon and one other)
- This can happen through Demon kills or mistaken executions

### Tie Resolution
- If both teams would win simultaneously (e.g., Demon executed leaving 2 players), good team wins

### Dead Players
- Dead players share victory or loss with their team
- Being dead does not change team alignment

## Special Mechanics

### First Night
- Some characters receive information on the first night
- Demon does not kill on the first night
- Setup information is given to certain characters

### Final Three
- When only 3 players remain, special rules may apply
- Mayor's ability activates in this situation
- Final day discussion before execution

### Travellers (16-20 Players)
- Known roles but hidden alignment
- Can join mid-game or leave early
- Do not count toward living player count
- Cannot be executed, only exiled (separate process)
- Cannot swap to non-Traveller roles

### Fabled Characters
- Controlled by Storyteller
- Used for game balance
- Not assigned to players
- Provide additional game mechanics

## Storyteller Responsibilities

### Information Management
1. Track all character abilities and their effects
2. Record information given to each player
3. Manage false information (poisoning, drunkenness)
4. Keep Grimoire organized and hidden

### Game Flow
1. Guide players through Night and Day phases
2. Ensure proper order of character activations
3. Manage voting and nominations
4. Resolve conflicts and rule questions

### Balance
1. Use discretion to provide fair information
2. Adjust difficulty through information given
3. Ensure both teams have a chance to win
4. Make the game enjoyable for all players

### Communication
1. Use silent signals during Night phase
2. Answer player questions clearly
3. Provide necessary information when abilities activate
4. Maintain game atmosphere and immersion

## App Development Considerations

### Essential Features
1. **Character Selection:** Randomly assign characters based on player count
2. **Night Phase Manager:** Wake characters in correct order, manage abilities
3. **Information Tracker:** Record what information each player has received
4. **Voting System:** Track nominations, votes, and executions
5. **Grimoire Interface:** Hidden view of all characters and game state
6. **Player Interface:** Show each player their role and any information received

### Technical Requirements
1. **Silent Communication:** Use visual/audio cues instead of physical signals
2. **State Management:** Track game phase, player status, ability usage
3. **Randomization:** Character assignment, information selection
4. **Data Persistence:** Save game state for mid-game breaks
5. **Multi-device Support:** Separate Storyteller and player views

### User Experience
1. **Clear Instructions:** Guide players through each phase
2. **Information Display:** Show abilities, reminders, and game state
3. **Error Prevention:** Prevent invalid actions and rule violations
4. **Accessibility:** Support for different devices and screen sizes
5. **Tutorial Mode:** Help new players learn the game

## References

- Official Blood on the Clocktower Wiki: https://wiki.bloodontheclocktower.com/
- Dicebreaker Rules Guide: https://www.dicebreaker.com/games/blood-on-the-clocktower/how-to/how-to-play-blood-on-the-clocktower-rules
- Official Game Website: https://bloodontheclocktower.com/



