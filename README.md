# Total-Surplus-Maximization---P2P


## Abstract
A fundamental component of e-commerce platform is ”Online Service Allocation (OSA)”, which matches service between producers and consumers. Existing systems focus on maximizing either of consumer utility or producer profit. We theorize, implement and test ”Total Surplus Maximization” which embodies the idea of maximizing total surplus (sum of producer and consumer surplus) in Online Service Allocation. We intend to implement and test the
hypothesis for online peer-to-peer lending data set and project results accordingly.

## Experiments/Dataset
We implement the hypothesis on Proper loans data set. Prosper is America’s first peer-to-peer lending marketplace where individuals can either invest in personal loans or request to borrow money. Investors can consider borrower’s credit scores, ratings, and histories and the category of the loan. Prosper handles the servicing of the loan and collects and distributes borrower payments and interest back to the loan investors. Here, borrower will specify two factors i.e., amount of money and max interest rate he is willing to accept for the loan. Lenders don’t have to provide all the requested amount,
they can only partly lend the amount requested by borrower

## Code Files
filter_sort_export.py - Used for taking raw data, preprocessing it and exporting to new data file.  
main_code.py - Main code