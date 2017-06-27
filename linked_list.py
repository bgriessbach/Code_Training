class Element(object):
	def __init__(self, value):
		self.value=value
		self.next=None
class LinkedList(object):
	def __init__(self, head=None):
		self.head=head
	
	def append(self, new_element):
		current=self.head
		if self.head:
			while current.next:
				current=current.next
			current.next=new_element
		else:
			self.head=new_element
	
	def get_position(self, position):
		count=1
		current=self.head
		if position<1:
			return None
		while current and count<=position:
			if count==position:
				return current
			current=current.next
			count+=1
		return None
	
	def insert(self, new_element, position):
		count=1
		if position==1:
			new_element.next=self.head
			self.head=new_element
		elif position>1:
			current=self.head
			while current and count<position:
				if count==position-1:
					new_element.next=current.next
					current.next=new_element
				current=current.next
				count+=1
				
	def delete(self, value):
		current=self.head
		past=None
		while current.next and current.value!=value:
			current=current.next
			past=current
		if past==None:
			self.head=current.next
		else:
			past.next=current.next


