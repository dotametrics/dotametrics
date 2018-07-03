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
