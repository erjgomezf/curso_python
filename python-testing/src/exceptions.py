class InsufficientFundsError(Exception):
    """Excepción para indicar que no hay fondos suficientes en la cuenta."""
    pass        

class withdrawTimeRestrictionsError(Exception):
    """Excepción para indicar que el retiro se intenta fuera del horario permitido."""
    pass