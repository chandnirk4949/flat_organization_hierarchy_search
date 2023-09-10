from django.db import models


#creating model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates')
    position = models.CharField(max_length=10, null=True, blank=True)  # 'left' or 'right' for head, it will we Null

# defining functions to retrieve the leftmost/rightmost child employee for the searched employee for the desired direction.
    def get_child_by_direction(self, direction):
        if direction == 'left':
            return self.get_leftmost_child_recursive()
        elif direction == 'right':
            return self.get_rightmost_child_recursive()
        else:
            return None

    def get_leftmost_child_recursive(self):
        leftmost_child = self.subordinates.filter(position='left').order_by('id').first() # type: ignore
        if leftmost_child:
            return leftmost_child.get_leftmost_child_recursive()
        rightmost_child = self.subordinates.filter(position='right').order_by('id').first() # type: ignore
        if rightmost_child:
            return rightmost_child.get_leftmost_child_recursive()
        return self

    def get_rightmost_child_recursive(self):
        rightmost_child = self.subordinates.filter(position='right').order_by('-id').first() # type: ignore
        if rightmost_child:
            return rightmost_child.get_rightmost_child_recursive()
        leftmost_child = self.subordinates.filter(position='left').order_by('-id').first() # type: ignore
        if leftmost_child:
            return leftmost_child.get_rightmost_child_recursive()
        return self