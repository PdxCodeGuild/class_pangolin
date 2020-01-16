
# UserClan: will only be created for clans of CCC users
# Will contain more detailed information about the clan (ie, roster)
# The key purpose of this object is to tie many other things together.  
# Other models use this as ForeignKey
# It is completely independent of the Clan class 
# class UserClan(models.Model):

#     # identifiers
#     userclan_wgid = models.IntegerField()
#     userclan_tag = models.CharField(max_length=10)
#     userclan_name = models.CharField(max_length=100)
    
#     # characteristics
#     # (will later add clan settings that can be modified by admirals)

#     # date created (for potential future DB maintenance)
#     date_created = models.DateTimeField(auto_now_add=True)