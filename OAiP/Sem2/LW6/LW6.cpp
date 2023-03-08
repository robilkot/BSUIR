// Вариант 5 - определить число узлов на каждом уровне дерева

#include <iostream>

struct treeNode
{
	treeNode(int content = 0, treeNode* left = nullptr, treeNode* right = nullptr) {
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

size_t nodesCount(treeNode* root, size_t targetLevel = 0, size_t currentLevel = 0)
{
	if (!root) return 0;

	return targetLevel == currentLevel ? 1
		: nodesCount(root->left, targetLevel, currentLevel + 1) + nodesCount(root->right, targetLevel, currentLevel + 1);
}

void showNodesCount(treeNode* root)
{
	size_t currentLevel = 0, currentLevelCount = nodesCount(root, 0);

	do {
		std::cout << "On level " << ++currentLevel << ": " << currentLevelCount << '\n';
		currentLevelCount = nodesCount(root, currentLevel);	
	} while (currentLevelCount != 0);
}

int main()
{
	treeNode* root = new treeNode; // 0 level (root)

	root->right = new treeNode; // 1st level
	root->left = new treeNode;

	root->right->right = new treeNode; // 2nd level
	root->right->left = new treeNode;
	root->left->right = new treeNode;

	root->right->left->right = new treeNode;  // 3rd level

	showNodesCount(root);
	
	deleteAll(root);
}