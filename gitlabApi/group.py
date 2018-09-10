# List groups
GET / groups

# create groups
post / groups
# groups_name groups_path is required
groups_name = ""
groups_path = ""
groups_visibility_level = ""


# delete groups
DELETE / groups / : id
#groups_id is requried
groups_id = ""

# List groups projects
GET / groups / : id/projects
#groups_id is requried
groups_id = ""

# List groups members
GET / groups / : id/members
#groups_id is requried
groups_id = ""

# Add groups member
POST / groups / : id/members
# groups_id groups_user_id groups_access_level is required
groups_id = ""
groups_user_id = ""
groups_access_level = ""

# Edit groups team member
PUT / groups /: id/members/: user_id
# groups_id groups_user_id groups_access_level is required
groups_id = ""
groups_user_id = ""
groups_access_level = ""

# Remove user team member
DELETE / groups /: id/members/: user_id
# groups_id groups_user_id is required
groups_id = ""
groups_user_id = ""
