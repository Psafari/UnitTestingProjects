import unittest
import os


import Blog_Backend

class flaskTestCase(unittest.TestCase):
    
    
    def test_index(self):
        tester1 = Blog_Backend.test_client(self)
        response = tester1.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'index.html')
        
    #To ensure that all expected parameters of the post are present in the database      
    def test_posts(self):
            self.assertIn("post_title", self.db.columns)
            self.assertIn("post_content ", self.db.columns)
            self.assertIn("post_author", self.db.columns)
            self.assertIn("new_post", self.db.columns)
            


    


    #Testing database
    def test_database(self):
        tester = os.path.exists("posts.db")
        self.assertTrue(tester)
        
        
        
if __name__ == '__main__':
    unittest.main()