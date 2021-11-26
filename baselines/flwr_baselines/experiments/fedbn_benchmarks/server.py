"""Flower server example."""


import flwr as fl

if __name__ == "__main__":
    strategy = fl.server.strategy.FedAvg(

        min_fit_clients=5,
        min_eval_clients=5,
        min_available_clients=5,
    )
    fl.server.start_server("[::]:8080", config={"num_rounds": 3}, strategy=strategy)
