# Exercise 1
def freeFall(val,isD):
    """
    g = 9.81 is the gravitational acceleration.

    When isD == True, use t = sqrt(2d/g) to calculate the falling time;
    When isD == False, use d = 0.5 * g * t^2 to calculate the distance travelled. 

    After calculation, round the result to second decimal digit as required.
    """
    
    g = 9.81

    # Calculate the falling time
    if isD:
        res = 2 * val / g
        res = res ** (0.5)
    # Calculate the distance travelled
    else:
        res = 0.5 * g * val ** 2

    res = round(res, 2)   
    return res 


# Exercise 2
def RPS(s):

    """
    First create a dictionary, where the key is a character ("S", "P", "R"),
    and the value is the corresponding winning character ("R", "S", "P").

    Then enumerate the string, get the winning string using the dictionary.
    """

    res = ""

    # A dictionary which takes a character and maps to 
    # its corresponding winning character
    map = {
        "S": "R",
        "P": "S",
        "R": "P"
    }

    # Scan the player's shape in each round
    # and attach the winning strategy to the result
    for ch in s:
        res += map[ch]

    return res 


# Exercise 3
def list2str(l):

    """
    Always use bracket "[" as the start for the results.

    Scan the list, for each element:

    if the element is character, then add it to the result string;
    if the element is list, the recusively call the function, add the return string to the string.

    After finish scanning the list, use "]" to contain the results.
    """

    res = "["

    # If element e is a list, then recursively call the function itself
    # otherwise append the letter to the result
    for e in l:
        if isinstance(e, list): 
            res += list2str(e)
        elif e.isalpha():
            res += e 

    res += "]"
    return res 


# Exercise 4
def textPreprocessing(text):

    """
    First, create a punctuation set, to remove the punctuation marks.

    Scan the string, for each character, if it is not in the punctuation set,
    then add it to a new string.

    Use lower function to convert characters to lowercases.

    Use split function to split the string, and get a list of words.

    Then create a stepword set, to remove the stepwords.

    Scan the word list, for each word, if it is not in the stepword set,
    then add it to a new list of words.

    Finally, do stemming, scan the word list, for each word,
    check if it ends with "s", "ed", or "ing" and change them to common base forms.

    """
    
    punctuation_set = set([".", "?", "!", ",", ":", ";", "-", "[", "]", "{", "}", "(", ")", "'", "\""])
   
    res = ""

    # Remove the punctuation marks
    for ch in text:
        if ch not in punctuation_set: 
            res += ch 

    # Convert the text to lower cases
    res = res.lower()

    # Seperate the words by spaces and get a list of words
    word_list = res.split()

    stepword_set = set(["i", "a", "about", "am", "an", "are", "as", "at", "be", "by", "for", \
        "from", "how", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "was", \
            "what", "when", "where", "who", "will", "with"])
    
    non_stepword_list = []
    
    # Remove the step words
    for word in word_list:
        if word not in stepword_set:
            non_stepword_list.append(word)

    res_list = []

    # Scan non-step words, and change them 
    # to common base forms if necessary
    for word in non_stepword_list:
        if word[-1] == "s":
            res_list.append(word[:-1])
        elif len(word) > 2 and word[-2:] == "ed":
            res_list.append(word[:-2])
        elif len(word) > 3 and word[-3:] == "ing":
            res_list.append(word[:-3])    
        else:
            res_list.append(word)

 
    return res_list


# Exercise 5
def isGreaterThan(dict1,dict2):

    """
    Intialize a variable is_strictly_greater to False,
    denoting whether dict1 is strictly greater than dict2 in at least one key.

    Check every key k1 in dict1, get corresponding value num1.
    Then get value num2 for k1 in dict2.

    Compare num1 and num2.

    If num1 < num2, then dict1 is strictly smaller than dict2 in at least one key.
    In this case, directly return False.

    If num1 > num2, then dict1 is strictly greater than dict2 in at least one key.
    In this case, set is_strictly_greater to True.

    Check every key k2 in dict2.
    Follow similar logics as above.

    If the two for loops go through, then it means
    dict1 is greater than or equal to dict2 with respect to all the keys.

    Then return is_strictly_greater.
    """

    is_strictly_greater = False

    for k1 in dict1:
        num1 = dict1[k1]
        # If dict2 does not contain k1, then get 0
        num2 = dict2.get(k1, 0)
        if num1 < num2: 
            return False
        if num1 > num2:
            is_strictly_greater = True

    for k2 in dict2:
        num1 = dict1.get(k2, 0)
        num2 = dict2[k2]
        if num1 < num2: 
            return False
        if num1 > num2:
            is_strictly_greater = True

    return is_strictly_greater


# Exercise 6
def CSVsum(filename):
    
    """
    Open the file, read each line of the file, and add it into a list of lines.

    If the first line is header (not a number), then start from the second line.

    Convert lines of strings to float numbers.

    Sum each column, and append the result to a list of numbers.
    
    """

    # lines will be a 2D array,
    # and lines[i] will be an array,
    # which contains strings in i-th line in the file,
    # seperated by commas (",")
    with open(filename) as file:
        lines = [line.split(",") for line in file]

    n = len(lines[0])
    res = [] 

    # If the first line is not numbers,
    # then start calculation from the second line
    if not lines[0][0].isnumeric():
        lines = lines[1:]

    # Convert strings in the array to float numbers
    nums = [list(map(float, line)) for line in lines] 

    # For each column, sum the numbers in that column,
    # append the sum to the result
    for i in range(n):
        res.append(sum(row[i] for row in nums))

    return res


# Exercise 7
def str2list(s):
    
    """
    Initialize an empty list first.

    Scan the string, maintain i as the current position, starting from 0.

    For each character in the string:

    if it is an alphabetical character, then add it to the result list;
    if it is "]", then return from the current function call (termination condition);
    if it is "[", then recursively call the function, and add the result to the list,
    and also moves the current position according to the length of the list from
    the recursive call;

    Terminate until the whole string is scanned.
    
    """
    res = []
    i = 0 

    while i < len(s):
        # Termination condition for the recursion,
        # return when there is a "]"
        if s[i] == "]":
            return res 
        # Start condition for the recursion,
        # when there is a "[" not at the beginning (i > 0);
        # move the cursor (i) using the length of the return sublist
        # to avoid repeatedly appending characters
        elif i > 0 and s[i] == "[":
            sublist = str2list(s[i:])
            res.append(sublist)
            i += len(sublist) + 1
        # If it is a letter, then just append it to the result
        elif s[i].isalpha():
            res.append(s[i])
        
        i += 1


# Exercise 8
def spacemonSim(roster1,roster2):
    
    """
    Create a map, where the key is the pair of attacking and defending spacemon,
    and the value is attack multipliers according to Table 1.

    Define a helper function spacemon_match(spacemon1, spacemon2),
    which takes two spacemons: spacemon1, spacemon2 as inputs,
    and outputs which one will win.
    The logic is to let spacemon1 and spacemon2 attack and defend,
    using the multiplier table, until the energy of one of them is <= 0.

    Scan the two input lists roster1 and roster2, for each pair of spacemons,
    call the helper function spacemon_match to tell which one wins.
    Proceed until one list has no remaining spacemons.
    """

    # A dictionary for attacking multiplier
    # according to Table 1
    multi_map = {
        ("Mercury", "Mercury"): 1.0,
        ("Mercury", "Venus"): 2.0,
        ("Mercury", "Earth"): 1.0,
        ("Mercury", "Mars"): 0.5,
        ("Venus", "Mercury"): 0.5,
        ("Venus", "Venus"): 1.0,
        ("Venus", "Earth"): 2.0,
        ("Venus", "Mars"): 1.0,
        ("Earth", "Mercury"): 1.0,
        ("Earth", "Venus"): 0.5,
        ("Earth", "Earth"): 1.0,
        ("Earth", "Mars"): 2.0,
        ("Mars", "Mercury"): 2.0,
        ("Mars", "Venus"): 1.0,
        ("Mars", "Earth"): 0.5,
        ("Mars", "Mars"): 1.0
    }

    # A helper function, which takes two spacemons,
    # and outputs which one will win,
    # and the remaining energy of the winning player
    def spacemon_match(spacemon1, spacemon2):
        planet1, energy1, power1 = spacemon1
        planet2, energy2, power2 = spacemon2
        
        while energy1 > 0 and energy2 > 0:
            energy2 -= multi_map[planet1,planet2] * power1 
            if energy2 <= 0:
                win = 1 
                player = planet1, energy1, power1
            energy1 -= multi_map[planet2,planet1] * power2
            if energy1 <= 0:
                win = 2
                player = planet2, energy2, power2

        return win, player

    cur_idx1, cur_idx2 = 0, 0
    cur_player1, cur_player2 = roster1[0], roster2[0]

    # Keep finding two spacemons from the two roster lists,
    # until one of them runs out of spacemons
    while cur_idx1 < len(roster1) and cur_idx2 < len(roster2):
        win, player = spacemon_match(cur_player1, cur_player2)
        if win == 1:
            cur_player1 = player 
            cur_idx2 += 1 
            if cur_idx2 >= len(roster2):
                return True
            cur_player2 = roster2[cur_idx2]
        elif win == 2: 
            cur_player2 = player
            cur_idx1 += 1
            if cur_idx1 >= len(roster1):
                return False
            cur_player1 = roster1[cur_idx1]


# Exercise 9
def rewardShortPath(env):
    
    """
    Firstly, define a helper function get_all_paths, implementing
    the idea in the Hint (enumerate all the paths from A to B),
    to get all the paths from A to B and store them in a list.

    Then check each path in the list, calculate the total distance
    and reward along the path, maintaining a minimum distance and
    maximum reward, and return the results.
    """

    # A helper function, which uses recursion and backtrack
    # to output all the paths from u to d
    # in a grid with size rows * cols;
    # the results (paths) will be appended into all_paths
    def get_all_paths(u, d, visited, path, rows, cols, all_paths):
        visited.add(u)
        path.append(u)

        if u == d:
            all_paths.append(path.copy())
        else:
            curr_r, curr_c = u
            neighbors = []
            if curr_r > 0:
                neighbors.append((curr_r-1, curr_c))
            if curr_r < rows - 1:
                neighbors.append((curr_r+1, curr_c))
            if curr_c > 0:
                neighbors.append((curr_r, curr_c-1))
            if curr_c < cols - 1:
                neighbors.append((curr_r, curr_c+1))

            for i in neighbors:
                neigh_r, neigh_c = i
                if i not in visited and env[neigh_r][neigh_c] != "X":
                    get_all_paths(i, d, visited, path, rows, cols, all_paths)

        path.pop()
        visited.remove(u)

    rows = len(env)
    cols = len(env[0])

    visited = set()
    path = []
    all_paths = []

    # start and end positions
    for r in range(rows):
        for c in range(cols):
            if env[r][c] == "A":
                start = r, c
            if env[r][c] == "B":
                end = r, c

    # Call the helper function to get
    # all the paths from start to end
    get_all_paths(start, end, visited, path, rows, cols, all_paths)

    min_dist = float("inf")
    max_reward = float("-inf")

    # Enumerate all the paths from A to B,
    # and calculate its distance and reward
    for i in range(len(all_paths)):
        curr_dist = 0
        curr_reward = 0

        curr_path = all_paths[i]

        for j in range(1, len(curr_path)):
            curr_dist += 1
            curr_r, curr_c = curr_path[j]
            if env[curr_r][curr_c] == "R":
                curr_reward += 1

        # Update the min_dist and max_reward
        # if the path has the shortest reward
        # or larger reward but it is one of the shorest paths
        if curr_dist < min_dist or (curr_dist == min_dist and curr_reward > max_reward):
            min_dist = curr_dist
            max_reward = curr_reward

    return min_dist, max_reward


# Exercise 10
def cliqueCounter(network):
    
    """
    https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

    Firstly, defnite a helper function Bron_Kerbosch, implementing the 
    Bron–Kerbosch algorithm in the Wikipedia link (without pivoting version),
    to get a list of all maximal cliques in the graph.

    Then check for each vertex in the graph, how many maximal cliques
    contain the vertex, and return the results.
    """

    # A helper function, which implements the
    # Bron–Kerbosch algorithm to get all the
    # maximal cliques in the graph;
    # the results will be in maximal_cliques
    def Bron_Kerbosch(R, P, X, maximal_cliques):
        if len(P) == 0 and len(X) == 0:
            maximal_cliques.append(set(R))
        for v in P[:]:
            R_new = R[::]
            R_new.append(v)

            P_new = [i for i in P if network[v][i] == 1]
            X_new = [i for i in X if network[v][i] == 1]
            
            Bron_Kerbosch(R_new, P_new, X_new, maximal_cliques)

            P.remove(v)
            X.append(v)

    maximal_cliques = []
    n = len(network)

    # Call the helper function to get the 
    # list of all maximal cliques
    Bron_Kerbosch([], list(range(n)), [], maximal_cliques)

    res_list = []

    # Check each node and calculate how many
    # maximal cliques contain the node
    # and append the number to the result
    for i in range(n):
        cnt = 0
        for max_clique in maximal_cliques:
            if i in max_clique:
                cnt += 1

        res_list.append(cnt)

    return res_list
