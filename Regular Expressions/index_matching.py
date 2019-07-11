for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index('money', 12, 51))
  except ValueError:
    print("substring not found")
