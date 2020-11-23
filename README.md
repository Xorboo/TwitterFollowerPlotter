# TwitterFollowerPlotter
See how many followers someones followers have, just in case you are weird like me and interested in that

## Example Output
![Example Output](img/example.png?raw=true "Example Output")
Also prints data into the console if you want to plot it yourself

## Notes
- You'll have to create your own bot and set up the keys in the code
- Twitter is limiting to ~15 requests per 15 minutes, each processing 200 followers only, so this can take a while for huge accounts. Passs `users_limit` parameter to limit processed users count
