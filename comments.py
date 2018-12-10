import queryhelp

def add_comments(comments, postObj):
# Adds comments to a existing post shared with a friend group. Takes in postObj
# dictionary object representing the post, the comment(s) to be added (each 
# comment is a tuple of the user and comment string) in chronological order.
# Example: comment[0] is the tuple (Jennifer, "That looks so delicious!")
    
    comments_list = list(comments)
    for item in comments_list:
        commentToBeAdded = {'Username': item[0], 'Comment': item[1]}
        postObj["comments"].append(commentToBeAdded)
        
        # Retrieves ID of post to which comments are to be added
        post_id = postObj["item_id"]
        
        # Inserts comment information into comments table of database
        query = "INSERT INTO comments(post_id, username, comment) VALUES (post_id, item[0], item[1]);"
        
        queryhelp.make_query(query, "i")