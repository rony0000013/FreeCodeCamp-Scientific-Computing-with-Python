import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**all_item):
        self.contents=[]
        for key,value in all_item.items():      # add the contents of the hat
            for idx in range(value):
                self.contents.append(key)       # add the name of the item
  
    # Function to get random n number of hats from contents
    def draw(self,amount):
        draw_list = []
        if amount >= len(self.contents):        # if the amount is larger than the number of items in the hat
            return self.contents
        for i in range(amount):
            name=self.contents.pop(random.randrange(len(self.contents)))    # remove the item from the hat
            draw_list.append(name)              # add the item to the list
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count=0
    for _ in range(num_experiments):            # run the experiment num_experiments times
      copyhat = copy.deepcopy(hat)
      temp_list = copyhat.draw(num_balls_drawn)
      success=True
      for key,value in expected_balls.items():  # check if the no of balls drawn is the same as the expected number
        if temp_list.count(key) < value:
          success=False
          break
      if success:
        final_count+=1
    return final_count/num_experiments



random.seed(95)
hat = Hat(blue=4, red=2, green=6)

probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
