#import os
#os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git

#repo_url = "https://github.com/PhonePe/pulse.git/"
#destination_path = "D:\Data Science\Project-2\Clone-repo"

c=git.Git("D:\Data Science\Project-2\Clone-repo").clone("https://github.com/PhonePe/pulse")