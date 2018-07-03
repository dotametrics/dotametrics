# dotametrics

read this in raw for proper formatting

0-Core Files
  d2slib -- Not mine, modified from the original: https://dev.dota2.com/showthread.php?t=48664
            Used to interact with the Dota2 API
  heroFileFix/modListFix -- Used to modify to heroList2 and modheroList2 when new heroes are added to the game
  heroList2 and modheroList2 -- Used by various other scripts for converting hero ID numbers to names
  
1-Sample Creation
  GetMatches* -- Various scripts to create a list of match IDs matches meeting specific critera
  GetMatchesAllDay -- May not have ever worked.  Suspect it was an aborted attempt to get around API issues
  MatchDetails* -- Takes the lists created by GetMatches* and creates a file with all the information for each individual match
  releaseCreator -- Used to release a comma separated export of MatchDetails for public consumption, 
                    ex: https://dotametrics.wordpress.com/2012/12/07/do-your-own-stats-the-player-data-dump/
  sampleCombine -- Used for combining the outputs of separate MatchDetails runs into a single file
  
  2-General Match Analysis
    avgStats -- Finds the average Kills per Minute, Assists per Minute, Creep Score per Minute, GPM and XPM of all the matches in a sample
                also finds averages among only winning teams and only losing teams
    durationR -- An early script for exporting stats into R.  Likely used in the creation of these graphs: https://dotametrics.wordpress.com/2012/11/07/very-high-skill-is-a-real-place-where-you-will-be-sent-at-the-first-sign-of-success/
    DurationStats -- Produces the duration distribution of a sample in 5-minute intervals
    radiantChart -- Finds the win rate of the Radiant side in separate 5-minute intervals to test how Radiant/Dire balance shifts with                         game duration.  Eventually lead to: https://www.liquiddota.com/forum/dota-2-general/460223-radiant-vs-dire-by-duration
    serverDist -- Displays the distribution of the server clusters used in the matches of a given sample
  
  3-Hero Usage Analysis
    1v1matchup -- Creates a matchup chart for hero win rates in the 1v1 mode:                                 https://dotametrics.files.wordpress.com/2014/06/1v1matchupchart.png
    boots -- Displays the distribution of endgame footwear ownership for every hero and their win rates
    farmDep -- The farm dependency test described here: https://dotametrics.wordpress.com/2013/04/16/hero-farm-dependency/
    heroDist -- Creates comma separated file of hero usage and win rates for spreadsheet import
    heroItem -- Finds the item usage and win rates for a particular hero
    newDuration3 -- Finds all heroes' win rates in short, medium and long duration matches, ex: https://dotametrics.wordpress.com/2014/03/10/hero-win-rates-by-match-duration-6-80-edition/
    SkillBasedClass -- converts a standard match aggregation file to the type of file used in SkillClassTest
    SkillClassTest -- finds the usage and win rates of various skill builds for a particular hero as an Excel import csv
ex: https://dotametrics.wordpress.com/2014/02/06/sbaphoenix-in-an-interstellar-burst-back-to-save-the-universe/  
    TotalItemList-- heroItem but for all players, ex: https://dotametrics.files.wordpress.com/2013/04/6-77items.png
    
    
    
