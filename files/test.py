from file_executor.write import write_to_file
from file_executor.delete import delete_file
from file_executor.create import create_file

create_file('albina', '.txt')
write_to_file("albina.txt", "67898765")
delete_file("albina.txt")