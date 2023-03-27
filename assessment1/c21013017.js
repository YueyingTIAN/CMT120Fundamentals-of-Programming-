const fs = require('fs');

module.exports = {

    // Exercise 1
    freefall: (val, isD) => {

        /*
        
        g = 9.81 is the gravitational acceleration.

        When isD == True, use t = sqrt(2d/g) to calculate the falling time;

        When isD == False, use d = 0.5 * g * t^2 to calculate the distance travelled. 

        After calculation, round the result to second decimal digit as required.

        */

        var g = 9.81;
        var res;

        // Calculate the falling time
        if (isD) {
            res = 2 * val / g;
            res = Math.sqrt(res);
        // Calculate the distance travelled
        } else {
            res = 0.5 * g * Math.pow(val, 2);
        }
        res = Math.round(res * 100) / 100;
        return res.toString();
    },


    // Exercise 2
    RPS: (play) => {

        /* 
        
        First create a dictionary, where the key is a character ("S", "P", "R"),

        and the value is the corresponding winning character ("R", "S", "P").

        Then enumerate the string, get the winning string using the dictionary.

        */

        // A dictionary which takes a character and maps to 
        // its corresponding winning character
        var map = new Map();
        map.set("S", "R");
        map.set("P", "S");
        map.set("R", "P");

        var res = "";

        // Scan the player's shape in each round
        // and attach the winning strategy to the result
        for (var i = 0; i < play.length; i++) {
            res += map.get(play[i]);
        }
        return res;
    },


    // Exercise 3
    list2str: (l) => {

        /* 
        
        Always use bracket "[" as the start for the results.

        Scan the list, for each element:

        if the element is character, then add it to the result string;
        if the element is list, the recusively call the function, add the return string to the string.

        After finish scanning the list, use "]" to contain the results.

        */

        var res = "["

        // If element e is a list, then recursively call the function itself
        // otherwise append the letter to the result
        for (var i = 0; i < l.length; i++) {
            if (Array.isArray(l[i])) {
                res += module.exports.list2str(l[i]);
            } else {
                res += l[i];
            }
        }
        res += "]"
        return res
    },


    // Exercise 4
    textPreprocessing: (text) => {
        /*
        
        First, create a punctuation set, to remove the punctuations marks.

        Scan the string, for each character, if it is not in the punctuation set,
        then add it to a new string.

        Use lower function to convert characters to lowercases.

        Use split function to split the string, and get a list of words.

        Then create a stepword set, to remove the stepwords.

        Scan the word list, for each word, if it is not in the stepword set,
        then add it to a new list of words.

        Finally, do stemming, scan the word list, for each word,
        check if it ends with "s", "ed", or "ing" and change them to common base forms.

        */


        var punctuation_set = new Set([".", "?", "!", ",", ":", ";", "-", "[", "]", "{", "}", "(", ")", "'", "\""]);

        var res = "";

        // Remove the punctuation marks
        for (var i = 0; i < text.length; i++) {
            if (punctuation_set.has(text[i]) === false) {
                res += text[i];
            }
        }

        // Convert the text to lower cases
        res = res.toLowerCase();

        // Seperate the words by spaces and get a list of words
        var word_list = res.split(" ");

        var stepword_set = new Set(["i", "a", "about", "am", "an", "are", "as", "at", "be", "by", "for",
            "from", "how", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "was",
            "what", "when", "where", "who", "will", "with"]);

        var non_stepword_list = [];

        // Remove the step words
        for (var i = 0; i < word_list.length; i++) {
            if (stepword_set.has(word_list[i]) === false) {
                non_stepword_list.push(word_list[i])
            }
        }

        var res_list = [];

        // Scan non-step words, and change them 
        // to common base forms if necessary
        for (var i = 0; i < non_stepword_list.length; i++) {
            var word = non_stepword_list[i];

            if (word.charAt(word.length - 1) === "s") {
                res_list.push(word.slice(0, -1));
            } else if (word.length > 2 && word.slice(-2) === "ed") {
                res_list.push(word.slice(0, -2));
            } else if (word.length > 3 && word.slice(-3) === "ing") {
                res_list.push(word.slice(0, -3));
            } else {
                res_list.push(word);
            }
        }

        return res_list;
    },


    // Exercise 5
    isGreaterThan: (dict1, dict2) => {
        /*
        
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

        */

        var is_strictly_greater = false;

        for (const [k1, num1] of Object.entries(dict1)) {

            if (k1 in dict2) {
                var num2 = dict2[k1];
            // If dict2 does not contain k1, then get 0
            } else {
                var num2 = 0;
            }

            if (num1 > num2) {
                is_strictly_greater = true;
            } else if (num1 < num2) {
                return false;
            }
        }

        for (const [k2, num2] of Object.entries(dict2)) {

            if (k2 in dict1) {
                var num1 = dict1[k2];
            } else {
                var num1 = 0;
            }

            if (num1 < num2) {
                return false;
            } else if (num1 > num2) {
                is_strictly_greater = true;
            }
        }

        return is_strictly_greater;
    },


    // Exercise 6
    CSVsum: (filename) => {
        /*
        
        Open the file, read each line of the file, and add it into a list of lines.

        If the first line is header (not a number), then start from the second line.

        Convert lines of strings to float numbers.

        Sum each column, and append the result to a list of numbers.

        */

        var array = fs.readFileSync(filename).toString().split("\n");
        var lines = [];

        // lines will be a 2D array,
        // and lines[i] will be an array,
        // which contains strings in i-th line in the file,
        // seperated by commas (",")
        for (var i = 0; i < array.length - 1; i++) {
            lines.push(array[i].split(","));
        }

        // If the first line is not numbers,
        // then start calculation from the second line
        if (isNaN(lines[0][0]) === true) {
            lines = lines.slice(1, lines.length);
        }

        var nums = [];

        // Convert strings in the array to float numbers
        for (var i = 0; i < lines.length; i++) {
            nums.push(lines[i].map(Number));
        }

        var n = lines[0].length;
        var res = [];

        // For each column, sum the numbers in that column,
        // append the sum to the result
        for (var i = 0; i < n; i++) {
            var sum = 0;
            for (var j = 0; j < nums.length; j++) {
                sum += nums[j][i];
            }
            res.push(sum)
        }

        return res;
    },


    // Exercise 7
    str2list: (s) => {
        /*
        
        Initialize an empty list first.

        Scan the string, maintain i as the current position, starting from 0.

        For each character in the string:

        if it is an alphabetical character, then add it to the result list;
        if it is "]", then return from the current function call (termination condition);
        if it is "[", then recursively call the function, and add the result to the list,
        and also moves the current position according to the length of the list from
        the recursive call;

        Terminate until the whole string is scanned.

        */

        var res = [];
        var i = 0;

        while (i < s.length) {

            // Termination condition for the recursion,
            //return when there is a "]"
            if (s[i] === "]") {
                return res
            // Start condition for the recursion,
            // when there is a "[" not at the beginning (i > 0);
            // move the cursor (i) using the length of the return sublist
            // to avoid repeatedly appending characters
            } else if (i > 0 && s[i] === "[") {
                var sublist = module.exports.str2list(s.slice(i, s.length));
                res.push(sublist);
                i += sublist.length + 1;
            // If it is a letter, then just append it to the result
            } else if (s[i] != "[") {
                res.push(s[i]);
            }
            i++;
        }

        return res;
    },


    // Exercise 8
    spacemonSim: (roster1, roster2) => {
        /*
        
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

        */


        // A dictionary for attacking multiplier
        // according to Table 1
        var multi_map = new Map();
        multi_map.set(["Mercury", "Mercury"].join(","), 1.0);
        multi_map.set(["Mercury", "Venus"].join(","), 2.0);
        multi_map.set(["Mercury", "Earth"].join(","), 1.0);
        multi_map.set(["Mercury", "Mars"].join(","), 0.5);
        multi_map.set(["Venus", "Mercury"].join(","), 0.5);
        multi_map.set(["Venus", "Venus"].join(","), 1.0);
        multi_map.set(["Venus", "Earth"].join(","), 2.0);
        multi_map.set(["Venus", "Mars"].join(","), 1.0);
        multi_map.set(["Earth", "Mercury"].join(","), 1.0);
        multi_map.set(["Earth", "Venus"].join(","), 0.5);
        multi_map.set(["Earth", "Earth"].join(","), 1.0);
        multi_map.set(["Earth", "Mars"].join(","), 2.0);
        multi_map.set(["Mars", "Mercury"].join(","), 2.0);
        multi_map.set(["Mars", "Venus"].join(","), 1.0);
        multi_map.set(["Mars", "Earth"].join(","), 0.5);
        multi_map.set(["Mars", "Mars"].join(","), 1.0);


        // A helper function, which takes two spacemons,
        // and outputs which one will win,
        // and the remaining energy of the winning player
        function spacemon_match(spacemon1, spacemon2) {
            var planet1 = spacemon1[0], energy1 = spacemon1[1], power1 = spacemon1[2];
            var planet2 = spacemon2[0], energy2 = spacemon2[1], power2 = spacemon2[2];

            while (energy1 > 0 && energy2 > 0) {
                energy2 -= multi_map.get([planet1, planet2].join(",")) * power1;
                if (energy2 <= 0) {
                    win = 1;
                    player = [planet1, energy1, power1];
                }
                energy1 -= multi_map.get([planet2, planet1].join(",")) * power2;
                if (energy1 <= 0) {
                    win = 2;
                    player = [planet2, energy2, power2];
                }
            }

            return [win, player];
        }

        var cur_idx1 = 0, cur_idx2 = 0;
        var cur_player1 = roster1[0], cur_player2 = roster2[0];
        var win = -1, player = [];

        // Keep finding two spacemons from the two roster lists,
        // until one of them runs out of spacemons
        while (cur_idx1 < roster1.length && cur_idx2 < roster2.length) {

            var results = spacemon_match(cur_player1, cur_player2);
            // console.log(results);

            win = results[0];
            player = results[1];

            if (win === 1) {
                cur_player1 = player;
                cur_idx2 += 1;
                if (cur_idx2 >= roster2.length) {
                    return true;
                }
                cur_player2 = roster2[cur_idx2];
            } else if (win === 2) {
                cur_player2 = player;
                cur_idx1 += 1;
                if (cur_idx1 >= roster1.length) {
                    return false;
                }
                cur_player1 = roster1[cur_idx1];
            }
        }
    },


    // Exercise 9
    rewardShortPath: (env) => {
        /*
        
        Firstly, define a helper function get_all_paths, implementing
        the idea in the Hint (enumerate all the paths from A to B),
        to get all the paths from A to B and store them in a list.

        Then check each path in the list, calculate the total distance
        and reward along the path, maintaining a minimum distance and
        maximum reward, and return the results.

        */

        // A helper function, which uses recursion and backtrack
        // to output all the paths from u to d
        // in a grid with size rows * cols;
        // the results (paths) will be appended into all_paths
        function get_all_paths(u, d) {
            visited.add(u.join(","));
            path.push(u);

            if (u.join(",") === d.join(",")) {
                all_paths.push(path.slice());
            } else {
                var curr_r = u[0], curr_c = u[1];
                var neighbors = [];
                if (curr_r > 0) {
                    neighbors.push([curr_r - 1, curr_c]);
                }
                if (curr_r < rows - 1) {
                    neighbors.push([curr_r + 1, curr_c]);
                }
                if (curr_c > 0) {
                    neighbors.push([curr_r, curr_c - 1]);
                }
                if (curr_c < cols - 1) {
                    neighbors.push([curr_r, curr_c + 1]);
                }

                for (var i = 0; i < neighbors.length; i++) {
                    var neighbor = neighbors[i];
                    var neigh_r = neighbor[0], neigh_c = neighbor[1];

                    if (visited.has(neighbor.join(",")) === false && env[neigh_r][neigh_c] != "X") {
                        get_all_paths(neighbor, d);
                    }
                }
            }

            path.pop();
            visited.delete(u.join(","));
        }

        var rows = env.length;
        var cols = env[0].length;

        var visited = new Set();
        var path = [];
        var all_paths = [];
        var start = [], end = [];

        // start and end positions
        for (var r = 0; r < rows; r++) {
            for (var c = 0; c < cols; c++) {
                if (env[r][c] == "A") {
                    start = [r, c];
                }
                if (env[r][c] == "B") {
                    end = [r, c];
                }
            }
        }

        // Call the helper function to get
        // all the paths from start to end
        get_all_paths(start, end);

        var min_dist = Number.MAX_VALUE;
        var max_reward = - Number.MAX_VALUE;

        // Enumerate all the paths from A to B,
        // and calculate its distance and reward
        for (var i = 0; i < all_paths.length; i++) {
            var curr_dist = 0, curr_reward = 0;

            var curr_path = all_paths[i];

            for (var j = 1; j < curr_path.length; j++) {
                curr_dist += 1;
                var curr_node = curr_path[j];
                var curr_r = curr_node[0], curr_c = curr_node[1];
                if (env[curr_r][curr_c] === "R") {
                    curr_reward += 1;
                }
            }

            // Update the min_dist and max_reward
            // if the path has the shortest reward
            // or larger reward but it is one of the shorest paths
            if (curr_dist < min_dist || curr_dist === min_dist && curr_reward > max_reward) {
                min_dist = curr_dist;
                max_reward = curr_reward;
            }
        }
        return [min_dist, max_reward]
    },

    
    // Exercise 10
    cliqueCounter: (network) => {
        /*
        
        https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

        Firstly, defnite a helper function Bron_Kerbosch, implementing the 
        Bron–Kerbosch algorithm in the Wikipedia link (without pivoting version),
        to get a list of all maximal cliques in the graph.

        Then check for each vertex in the graph, how many maximal cliques
        contain the vertex, and return the results.

        */

        // A helper function, which implements the
        // Bron–Kerbosch algorithm to get all the
        // maximal cliques in the graph;
        // the results will be in maximal_cliques
        function Bron_Kerbosch(R, P, X) {

            if (P.length === 0 && X.length === 0) {
                maximal_cliques.push(new Set(R.slice()));
            }

            var P_original = P.slice();
            for (var i = 0; i < P_original.length; i++) {
                var v = P_original[i];
                var R_new = R.slice();
                R_new.push(v);

                var P_new = [];
                for (var j = 0; j < P.length; j++) {
                    if (network[v][P[j]] === 1) {
                        P_new.push(P[j]);
                    }
                }

                var X_new = [];
                for (var j = 0; j < X.length; j++) {
                    if (network[v][X[j]] === 1) {
                        X_new.push(X[j]);
                    }
                }

                Bron_Kerbosch(R_new, P_new, X_new);

                var index = P.indexOf(v);
                P.splice(index, 1)
                X.push(v);
            }
        }

        var maximal_cliques = [];
        var n = network.length;

        var p = [];
        for (var i = 0; i < n; i++) {
            p.push(i);
        }

        // Call the helper function to get the 
        // list of all maximal cliques
        Bron_Kerbosch([], p, []);

        var res_list = [];

        // Check each node and calculate how many
        // maximal cliques contain the node
        // and append the number to the result
        for (var i = 0; i < n; i++) {
            var cnt = 0;
            for (var j = 0; j < maximal_cliques.length; j++) {
                var max_clique = maximal_cliques[j];
                if (max_clique.has(i) === true) {
                    cnt += 1;
                }
            }
            res_list.push(cnt);
        }
        return res_list
    }

}
