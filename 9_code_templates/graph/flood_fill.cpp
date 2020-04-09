//component(i) denotes the
//component that node i is in
void flood_fill(new_component)
	do
		num_visited = 0
		for all nodes i
			if component(i) = -2
				num_visited = num_visited + 1
				component(i) = new_component

	for all neighbors j of node i
		if component(j) = nil
			component(j) = -2
			until num_visited = 0

void find_components()
	num_components = 0

	for all nodes i
		component(node i) = nil
	
	for all nodes i
		if component(node i) is nil
			num_components = num_components + 1
			component(i) = -2
			flood_fill(component num_components)