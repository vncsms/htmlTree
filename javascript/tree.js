class Tree {
	constructor(value) {
		this.value = value;
		this.parent = null;
		this.children = [];
	}

	addChild(node) {
		node.parent = this
		this.children.push(node)
	}
}