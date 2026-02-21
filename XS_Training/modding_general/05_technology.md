# Modding - Technology Attributes and Effects

## Technology Attributes

### Full Tech Mode

- `0` - Available in full tech tree (for civilization specific techs)
- `1` - Disabled in FTT
- Available only in the following game mode. Negative value for disable in that game mode (except `32`)
- `2` - Random map
- `3` - Deathmatch
- `4` - Empire Wars or Empire Wars Mode
- `5` - Wonder Race
- `6` - Defend the Wonder
- `7` - Sudden Death or Sudden Death Mode
- `8` - King of the Hill
- `9` - Capture the Relic
- `10` - Battle Royale
- `11` - Regicide
- `12` - Turbo Mode
- `13` - Scenario or Campaign game
- `14` - Regicide Mode
- `15` - Scenario Editor
- `16` - D3
- `17` - Solid Farms
- `18` - Shared Exploration
- `19` - Default Starting Resources
- `20` - Low Starting Resources
- `21` - Medium Starting Resources
- `22` - High Starting Resources
- `23` - Ultra-High Starting Resources
- `24` - Infinite Starting Resources
- `25` - Random Starting Resources
- `26` - Antiquity mode
- New: `27` - Dark Age Start
- New: `28` - Feudal Age Start
- New: `29` - Castle Age Start
- New: `30` - Imperial Age Start
- New: `31` - Post-Imperial Age Start
- New: `32` - Feudal Age Start or later
- New: `33` - Castle Age Start or later
- New: `34` - Imperial Age Start or later

## Technology Effects

- Tech Cost Modifier and Tech Time Modifier with Mode `2` will multiply technology costs or time by the specified amount.
- Resource to `-1` in Tech Cost Modifier effect will target all costs of the technology.
- Technology cost and time adjustment values now stack with the previously applied adjustments instead of overwriting them.
- Added new Modify Technology actions:
  - `-3` - Multiply Tech Time
  - `13` - Multiply Food Cost
  - `14` - Multiply Wood Cost
  - `15` - Multiply Stone Cost
  - `16` - Multiply Gold Cost
  - `17` - Multiply All Costs
