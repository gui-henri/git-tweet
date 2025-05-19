# .git/hooks/tweet.ps1

# Get the latest commit message
$commitMessage = git log -1 --pretty=%B

# Write to console for now
Write-Output "Generating tweet for: $commitMessage"

# Calling Python script
$scriptPath = "$PSScriptRoot\tweet.py"
& python $scriptPath "$commitMessage"