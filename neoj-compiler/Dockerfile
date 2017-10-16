FROM microsoft/aspnetcore:1.0.4

WORKDIR /compile/src

COPY ./org.neo.smartcontract.framework.jar /usr/share/dotnet
COPY ./submodule-neo-compiler/neoj/out /compile

ENTRYPOINT ["dotnet", "/compile/neoj.dll"]