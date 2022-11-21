class ClienteValidate:
    def validate(cliente):
        msg = []

        if(cliente.getNome() == ""):
            msg.append("Favor preencher o nome !")
        if(cliente.getEmail() == ""):
            msg.append("Favor preencher o email !")
        return msg