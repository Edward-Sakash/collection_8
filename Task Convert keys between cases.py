"""ask - Convert keys between cases
Different programming languages use different kind of schemes to name things. For example Python uses snake_case, JavaScript uses camelCase. You might also come across kebap-case - sometimes also called dash-case. You can read more about naming conventions in programming the matching Wikipedia article.

When an API you are using is implemented using a different language it might not match Python's convention of naming things. Hence your task is to implement a method that converts a dictionary with natural cased keys like A random key to a_random_key.

Input A:
natural_case = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}
Output A:
snake_case = {
  'company_name': 'Digital Career Institute',
  'street': 'Vulkanstraße',
  'house_number': 1,
  'city': 'Berlin'
}
Input B:
natural_case = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}
Output B:
snake_case = {
  'movie_name': 'James Bond 007: Skyfall',
  'director': 'Sam Mendes',
  'production_year': 2012,
  'duration_in_minutes': 143,
  'production_countries': ['US', 'UK']
}"""

# Solution 1

natural_case_A = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}
natural_case_B = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}

snake_case_A = {}
snake_case_B = {}

# Loop through each key-value pair in the original dictionary
for key, value in natural_case_A.items():
    # Convert the key from natural case to snake case
    snake_key_A = key.lower().replace(' ', '_')
    # Add the new key-value pair to the new dictionary
    snake_case_A[snake_key_A] = value

for key, value in natural_case_B.items():
    # Convert the key from natural case to snake case
    snake_key_B = key.lower().replace(' ', '_')
    # Add the new key-value pair to the new dictionary
    snake_case_B[snake_key_B] = value    

print(snake_case_A)
print(snake_case_B)
