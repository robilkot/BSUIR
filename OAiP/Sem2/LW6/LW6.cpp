#include <iostream>

struct treeNode
{
	treeNode(int content, treeNode* left = nullptr, treeNode* right = nullptr) {
		this->content = content;
		this->left = left;
		this->right = right;
	}

	int content = 0;
	treeNode* left = nullptr;
	treeNode* right = nullptr;
};

void deleteAll(treeNode* root)
{
	treeNode* left = root->left;
	treeNode* right = root->right;
	
	delete root;

	if (left) deleteAll(left);
	if (right) deleteAll(right);
}

int nodesCount(treeNode* root, size_t targetLevel = 0, size_t currentLevel = 0)
{

}

int main()
{
	treeNode* root = new treeNode(1);
	root->right = new treeNode(1);
	root->left = new treeNode(1);
	root->right->right = new treeNode(1);
	root->right->left = new treeNode(1);

	std::cout << nodesCount(root, 0) << '\n';
	std::cout << nodesCount(root, 0) << '\n';
	
	std::cout << nodesCount(root, 1) << '\n';
	std::cout << nodesCount(root, 1) << '\n';
	
	std::cout << nodesCount(root, 2) << '\n';
	std::cout << nodesCount(root, 2) << '\n';
	
	deleteAll(root);
}