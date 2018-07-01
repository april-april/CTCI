def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' %
                            node.label)

        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])

        # Assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break  