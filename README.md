# Projet Qwen Skills

## Prerequisites

- [Node.js](https://nodejs.org/) installed
- Windows PowerShell 5.1+

## Windows Setup: PowerShell Execution Policy

By default, PowerShell blocks script execution (`Restricted` policy), which prevents `npm` and other Node.js tools from running.

### Configure the execution policy

Run the following command in PowerShell to permanently allow local scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

This sets the policy for your user account only — no admin rights required. `RemoteSigned` allows local scripts to run while requiring downloaded scripts to be signed.

### Verify the configuration

Check that the policy is correctly set:

```powershell
Get-ExecutionPolicy -List
```

Expected output:

```
        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser    RemoteSigned
 LocalMachine       Undefined
```

### Quick fix for a single session

If you only need to unblock scripts temporarily:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

This resets when the terminal is closed.

## Installing Dependencies

```powershell
npm install -g qwen-superpowers
```
