// Creator: Derek Goh | FIT1055 - A3
// Date: 11 May 2024

pragma solidity >=0.5.8;

contract WMHashStorage {
    struct Transaction {
        string transactionID;
        string dataHash;
    }

    mapping(string => Transaction) private transactions;
    uint public transactionCount = 0;

    function store(string memory _transactionId, string memory _dataHash) public {
        Transaction memory newTransaction = Transaction(_transactionId, _dataHash);
        transactions[_transactionId] = newTransaction;
        transactionCount++;
    }

    function getData(string memory _transactionId) public view returns (string memory) {
        return transactions[_transactionId].dataHash;
    }

    function getTransactionCount() public view returns (uint) {
        return transactionCount;
    }
}