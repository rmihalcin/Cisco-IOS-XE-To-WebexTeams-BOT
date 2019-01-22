1.	from ciscosparkapi import CiscoSparkAPI  

2.	  

3.	if __name__=='__main__':  

4.	    # Use ArgParse to retrieve command line parameters.  

5.	    from argparse import ArgumentParser  

6.	    parser = ArgumentParser("Spark Check In")  

7.	    # Retrieve the Spark Token and Destination Email  

8.	    parser.add_argument(  

9.	        "-t", "--token", help="Spark Authentication Token", required=True  

10.	    )  

11.	    # Retrieve the Spark Token and Destination Email  

12.	    parser.add_argument(  

13.	        "-e", "--email", help="Email to Send to", required=True  

14.	    )  

15.	    args = parser.parse_args()  

16.	    token = args.token  

17.	    email = args.email  

18.	    message = "**Alert:** Router in Config Mode"  

19.	    api = CiscoSparkAPI(access_token=token)  

20.	    api.messages.create(toPersonEmail=email, markdown=message)  
