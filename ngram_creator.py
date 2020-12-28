#function to create bigrams or trigrams
def anagram_creation(my_list, desired_len):
  def anagram_prep(my_list, desired_len):
    if len(my_list) % desired_len == 0:
      return my_list
    if len(my_list) % desired_len == 1:
      my_list.remove(my_list[len(my_list)-1])
      return my_list
    if len(my_list) % desired_len == 2:
      my_list.remove(my_list[len(my_list)-1])
      my_list.remove(my_list[len(my_list)-1])
      return my_list
    if len(my_list) % desired_len > 2:
      return my_list

  
  working_list = anagram_prep(my_list, desired_len)
  if desired_len == 2:
    output_list = []
    times_calculations_run = len(working_list) / 2
    my_counter = 0
    bigram_one = 0
    bigram_two = 1

    while my_counter != times_calculations_run:
      bigram_element = working_list[bigram_one] + " " + working_list[bigram_two]
      output_list.append(bigram_element)
      my_counter += 1
      bigram_one += 2
      bigram_two += 2

  if desired_len == 3:
    output_list = []
    times_calculations_run = len(working_list) / 3
    my_counter = 0
    trigram_one = 0
    trigram_two = 1
    trigram_three = 2

    while my_counter != times_calculations_run:
      trigram_element = working_list[trigram_one] + " " + working_list[trigram_two] + " " + working_list[trigram_three]
      output_list.append(trigram_element)
      my_counter += 1
      trigram_one += 3
      trigram_two += 3
      trigram_three += 3

  return output_list
