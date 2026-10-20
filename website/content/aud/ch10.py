CH = {
 'n': 10,
 't': 'IT-Based Audit Assurance',
 'brief': 'Auditing in a computerised environment: the six types of information technology '
          'system, the special challenges of small (PC-based) systems, how audit documentation '
          'and the audit approach itself change with IT, Computer Assisted Audit Techniques '
          '(CAATs), application vs. general controls in a computer environment, controls in '
          'online/real-time systems and database management systems, business/IT risk, and '
          'the current technology trends reshaping audit practice — big data, electronic '
          'transaction audit, artificial intelligence and machine learning.',
 'outcomes': [
   'Explain types of information technology systems that auditors encounter',
   'State typical control challenges faced in the assurance of small IT-based systems',
   'Explain documentation procedures used in the assurance of manual and IT-based systems',
   'Explain the approach to the audit of IT-based systems with attention to audit trail and '
   'controls',
   'Explain business systems and associated IT risks',
   'Explain the concepts of IT audit activities and current trends in Information Technology '
   '(big data analytics, audit of electronic transactions, artificial intelligence, machine '
   'learning)',
 ],
 'secs': [
  {'n': '10.1', 't': 'Information technology systems', 'b': [
    {'p': 'There are six information technology systems an auditor encounters:'},
    {'table': {'align': 'll', 'head': ['System', 'What it does'], 'rows': [
      ['**Transaction Processing System (TPS)**', 'Turns transaction inputs into outputs — a '
       'transaction includes all purchases/sales of goods/services and business activities '
       'needed to run the entity. Originally called "data processing"; an improvement over '
       'manual handling.'],
      ['**Office Automation System (OAS)**', 'A web of tools/technologies for clerical and '
       'managerial tasks — recording, printing, mailing.'],
      ['**Knowledge Management System (KMS)**', 'Stores and extracts information to help '
       'employees/customers/management build knowledge and optimise collaboration — the '
       'shared information may itself be the product (e.g. in education) or about the product '
       '(e.g. commercial/industrial settings).'],
      ['**Management Information System (MIS)**', 'Lets middle managers extract transaction '
       'data from a TPS, analyse it, and produce reports helping top management optimise '
       'planning/decision-making — including summarisation into the entity\'s financial '
       'statements.'],
      ['**Decision Support System (DSS)**', 'Software tools (e.g. Microsoft Office) assisting '
       'management decisions — spelling/grammar correction (Word), large-volume calculation/'
       'variance analysis/scenario mapping (Excel) — helping middle managers make informed '
       'decisions.'],
      ['**Executive Support System (ESS)**', 'Also called an "expert system" — proffers '
       'solutions to non-routine problems (e.g. taxation, investment, shareholding '
       'information), helping directors/owners monitor entity performance.'],
    ]}},
    {'key': 'Understanding these six systems helps the auditor identify which information '
            'system is of **particular importance** to the audit versus which is secondary — '
            'but every IT system in use at the client is relevant to the auditor\'s overall '
            'knowledge of the client\'s business.'},
  ]},

  {'n': '10.2', 't': 'Challenges faced by small IT-based systems', 'b': [
    {'key': 'Most PC-related control problems arise from the **departure from the formal '
            'structure** of a traditional data processing department — the world of the PC is '
            'more informal, lacking the controlled environment traditionally provided over '
            'acquisition, maintenance and distribution of computer information.'},
    {'p': 'Problems surrounding PCs fall under three headings, each creating difficulty '
          'assessing documentation, design-process adequacy, and the completeness/accuracy/'
          'authority of data and audit trails:'},

    {'h4': '§10.2.1 Lack of planning over acquisition and use'},
    {'table': {'align': 'll', 'head': ['Consideration', 'What it involves'], 'rows': [
      ['**Authorization**', 'A feasibility study examining requirements/costs/benefits; '
       'inviting supplier tenders and comparing responses; involving all interested parties '
       'throughout; ideally consulting other system users (e.g. the auditors themselves) for '
       'their opinion.'],
      ['**Suitability**', 'Risk that the client lacks the expertise to properly evaluate '
       'systems, causing compatibility/capacity problems that restrict future development '
       '(short of full replacement). Standard software packages purchased by first-time users '
       'raise this risk further, since they may not precisely fit the company\'s trading '
       'methods, and first-time users are unlikely to have the expertise to tailor them.'],
      ['**Support facilities**', 'The client should ascertain supplier/software-house support '
       'and enter a maintenance contract ensuring: prompt service (and backup facilities) on '
       'breakdown; bugs can be sorted out; minor modifications are possible; adequate systems '
       'documentation (program documentation, operator instructions, and a user manual) and '
       'operator manuals are provided; and operators receive adequate instruction.'],
      ['**Standards**', 'A formal data processing environment normally has hardware/software '
       'standards for controls and accounting principles — but with PCs, where ordering-to-'
       'operation may take only weeks, there is a real danger standards are never set. Strict '
       'discipline is needed to apply recognised systems-development controls and sufficient '
       'administration procedures.'],
    ]}},

    {'h4': '§10.2.2 Lack of documentary evidence'},
    {'p': 'Many PCs operate in real time via VDUs, giving users direct computer access to '
          'input data, update files and make one-off enquiries — avoiding the need for edit '
          'programs and hard copy. Control can be enhanced by building in edit programs at the '
          'design stage, and incorporating a **user-usage file** logging user identification, '
          'the application involved, and records accessed/updated — periodically reviewed by a '
          'responsible official and the auditor. Manual controls (transactions only processed '
          'with a supporting initiating document, manual batching) may also be prudent.'},

    {'h4': '§10.2.3 Lack of security and confidentiality'},
    {'table': {'align': 'll', 'head': ['Problem', 'Detail'], 'rows': [
      ['**Lack of segregation of duties**', 'The same person often prepares data, feeds it in, '
       'supervises processing, and is the end user — enhancing fraud opportunity via combined '
       'access to assets and their recording/disposal. Auditors may need extensive substantive '
       'verification work to compensate.'],
      ['**Lack of control over users**', 'PCs do not require a protected environment, so '
       'terminals are readily available to any user — necessitating controls preventing '
       'unauthorised use (locks, passwords, etc.).'],
      ['**Lack of control over program alterations**', 'A lack of expertise may cause imprudent '
       'purchase decisions; conversely, expertise is easily acquired once a machine is '
       'operational (PCs use high-level languages, learnable quickly), risking undetected '
       'program alteration, or programs written without adequate testing while data is being '
       'processed. Stringent supervisory arrangements and programmed controls preventing '
       'unauthorised running are needed. Programs permanently etched onto silicon chips (ROMs) '
       'gain security since only specialist electronics engineers can alter them.'],
    ]}},
  ]},

  {'n': '10.3', 't': 'Documentation procedures in IT-based systems', 'b': [
    {'p': 'Computerised working paper packages ease documenting audit work, aiding preparation '
          'of working papers, lead schedules, extended trial balances and financial statements '
          '— automatically cross-referenced and balanced, with adjustments automatically '
          'updating all necessary schedules.'},
    {'p': 'Advantages of automated working papers: reduced risk of errors; neater, easier-to-'
          'review papers; substantial time saved (adjustments apply easily across all papers, '
          'including analytical summaries); no need to carry standard forms to audit locations '
          '(forms can be called up/completed on screen); and working papers can be transmitted '
          'for review via the internet.'},
    {'p': 'Combining office packages (Word, Excel, Access) can automate logical steps: '
          '**checking completeness** (is there evidence of supervision/review on each '
          'schedule? Is there an audit conclusion on each lead schedule? Have all points on '
          '"audit point sheets" been answered?); **checking accuracy** (are numeric totals '
          'consistent? Do they carry forward accurately to the lead schedule?); and '
          '**automated processing** (footing/cross-footing, carrying forward numeric data to '
          'lead schedules, highlighting proposed recommendations for management review, '
          'consolidating/reformatting material for the draft audit report). More generally, '
          'graphics production, image processing, desk-top publishing, and on-line/real-time '
          'file access can all assist.'},
    {'key': 'Software packages can also perform **analytical procedures** and **statistical '
            'sampling** — most useful when imputed directly from the client\'s own system, '
            'building cumulative year-on-year data, and able to determine sample sizes, '
            'generate random numbers, and evaluate sample-based test results.'},
    {'p': 'Decision support systems automate judgmental processes normally requiring a "human" '
          'auditor — notably automating checklists (internal control evaluation, statutory '
          'requirements, materiality estimation) that follow different logic paths depending '
          'on answers given, including omitting questions where appropriate.'},
  ]},

  {'n': '10.4', 't': 'Audit approach in IT-based systems', 'b': [
    {'p': 'Audits are performed "in a computer environment" wherever computer-based accounting '
          'systems (large or small) process information supporting the financial statements — '
          'operated by the entity itself, or by a third party on its behalf.'},
    {'def': {'t': 'Computer Assisted Audit Techniques (CAATs)', 'd': 'techniques performed with '
                  'computers by the auditor, in two major categories: (a) use of audit '
                  'software — computer programs examining the enterprise\'s computer file '
                  'contents; and (b) use of test data — data used by the auditor to test the '
                  'operation of the enterprise\'s own computer programs.'}},
    {'key': 'When auditing in a computer environment, the auditor needs a basic understanding '
            'of data-processing fundamentals, and technical computer knowledge/skill that may, '
            'depending on circumstances, need to be **extensive**.'},

    {'h4': 'Planning the use of CAATs'},
    {'p': 'Points to weigh when choosing between CAATs and manual procedures:'},
    {'ol': [
      'computer programs often perform functions with **no visible evidence** — making manual '
      'testing frequently impracticable;',
      'where a manual/CAAT choice genuinely exists, the auditor weighs relative efficiency: '
      'the extent of test-of-control/substantive coverage each achieves, the CAAT\'s cost '
      'pattern, and its ability to incorporate several different tests at once;',
      'under a short reporting time-scale, CAATs may be more efficient (quicker to apply) even '
      'if manual methods remain practicable and cheaper;',
      'using a CAAT requires ensuring the necessary computer facilities/files/programs are '
      'available, and — since enterprises don\'t retain copies indefinitely — planning in good '
      'time to preserve copies and avoid **loss of audit trail**;',
      'some CAATs need frequent auditor attendance/access; reliance on internal auditors\' own '
      'CAATs depends on the assessed effectiveness/relevance of the internal audit function; '
      'and',
      'where accounting records include computer data, the auditor needs access to it — '
      'current practice often uses auditor laptops to test client data collected from the '
      'client\'s system, without entering that system directly.',
    ]},
    {'key': 'Where CAATs are used, particular attention is needed on: co-ordinating specialist-'
            'computer-skilled staff with the rest of the audit team; and approval/review of '
            'the technical work by someone with the necessary computer expertise. A CAAT may '
            'be used on copies of computer records/programs, provided reasonable assurance is '
            'gained that the copies are **identical to the originals**.'},

    {'h4': 'Internal control evaluation in a computer environment'},
    {'key': 'The same internal-control principles apply as in any environment, with '
            'additional considerations. Controls split into **application controls** '
            '(specific to each transaction/standing-data system, ensuring completeness/'
            'accuracy of records and validity of entries from manual and programmed '
            'processing) and **general controls** (relating to the whole environment in which '
            'computerised operations occur, ensuring proper development/implementation of '
            'applications and program/data/operations integrity). Both may be manual or '
            'programmed.'},
    {'p': 'Where preliminary evaluation reveals absent or uncompensated-weak controls, the '
          'auditor moves directly to substantive procedures (possibly CAAT-assisted). Where '
          'controls may meet the auditor\'s objectives, tests of controls follow if reliance is '
          'wanted — influenced by cost-effectiveness, ease of testing, and reliability factors. '
          'Procedures for testing controls include: observing the control in operation; '
          'examining documentary evidence of its operation; repeat performance; and testing/'
          're-performing specific program parts via CAATs for programmed controls.'},

    {'h4': 'Review, working papers and audit trails'},
    {'p': 'CAATs (particularly audit software) can assist aspects like analytical review. '
          'Where a CAAT is used, working papers should show: the work performed, its results, '
          'the auditor\'s conclusions, how technical problems were resolved, and any '
          'recommendations for modifying the CAAT in future audits.'},
    {'key': 'An audit trail\'s original purpose was to preserve **paper** details of every '
            'processing stage — letting a transaction be followed stage-by-stage (e.g. a sales '
            'transaction traced through the customer order, delivery note, invoice and cheque/'
            'cash receipt) to confirm correct processing.'},

    {'h4': 'Around the computer vs. through the computer'},
    {'table': {'align': 'll', 'head': ['Approach', 'How it works'], 'rows': [
      ['**Around the computer** (traditional)', 'Auditors fulfil their function without '
       'detailed knowledge of what happens inside the computer — ignoring internal program '
       'procedures and concentrating solely on inputs/outputs (checking authorisation/coding/'
       'control totals of inputs, and outputs against source documents/clerical control '
       'totals). Consumes vast paper/computer/printer time, and does not reflect modern '
       'computerised accounting reality (computers manipulate/interpret data for management as '
       'much as record-keeping) — as system complexity has increased, audit trail has '
       'correspondingly been lost, and this approach is now frowned upon.'],
      ['**Through the computer** (modern default)', 'Examines the computer\'s detailed '
       'processing routines to determine whether controls adequately ensure complete/correct '
       'processing of all data — often requiring CAATs. Addresses typical problems as trails '
       'move away from hard copy: testing computer-generated totals absent detailed analysis, '
       'and testing output completeness absent control totals. The principal challenge is '
       'acquiring genuine understanding of electronic data processing and the computer '
       'itself.'],
    ]}},
  ]},

  {'n': '10.5', 't': 'Computer Assisted Audit Techniques (CAATs) in detail', 'b': [
    {'p': 'There is nothing mysterious about using a computer to help audit — most modern '
          'accounting systems allow ad-hoc reporting and sophisticated database querying; even '
          'limited systems let data be exported to a spreadsheet for sorting/recalculation; and '
          'most systems have search facilities far quicker than manual print-out searching, '
          'offsetting much of the so-called "loss of audit trail" (the trail is still there, '
          'just followed electronically).'},
    {'key': 'Before running any audit software, the auditor checks the **identity and version** '
            'of the data files/programs used (client-supplied or auditor-supplied), normally '
            'via external evidence like control totals, file lengths, dates and other file '
            'properties.'},

    {'h4': 'Audit interrogation software'},
    {'p': 'Performs the checks on data auditors would otherwise do by hand — particularly '
          'appropriate for substantive testing of transactions and balances, letting the '
          'auditor scrutinise large data volumes while concentrating skilled manual resources '
          'on investigating results rather than extracting information. Considerations: a '
          'basic understanding of data processing/the application, plus detailed knowledge of '
          'the audit software and files used; possibly a sound appreciation of systems '
          'analysis/operating systems, and programming-language experience if program code is '
          'used; how easily client data transfers to the auditor\'s PC; and whether the client '
          'can fully explain all the information their system produces.'},

    {'h4': 'Test data'},
    {'p': 'Inputting test data and comparing actual results against pre-calculated expected '
          'results tests whether a system processes data correctly. The problem: any resulting '
          'data-file corruption must be corrected, which is difficult with modern real-time '
          'systems (whose built-in controls often prevent easy, mark-free removal of entered '
          'data) — consequently, test data is falling out of use as a CAAT.'},

    {'h4': 'Embedded audit facilities'},
    {'key': 'Test data results would be completely distorted if the programs processing it '
            'were not the ones normally used (e.g. a fraudulent IT staff member substituting a '
            'correct-result version purely during the test). **Embedded audit facilities** — '
            'audit modules incorporated directly into the enterprise\'s own accounting system — '
            'allow continuous review instead.'},
    {'table': {'align': 'll', 'head': ['Technique', 'How it works'], 'rows': [
      ['**Integrated Test Facility (ITF)**', 'Creates a fictitious entity (e.g. a department '
       'or customer) within the regular application; transactions are posted to it alongside '
       'real transactions, and the results are compared against a predetermined expected '
       'outcome. Care is needed to keep the fictitious entity out of actual financial '
       'reporting — the simplest, most secure method being reversing journal entries at '
       'appropriate cut-off dates. ITF lets management and auditors constantly check internal '
       'processing functions on both valid and invalid transactions.'],
      ['**System Control and Review File (SCARF)**', 'Relatively simple to build in — e.g. for '
       'a general ledger, each account carries two "auditor" fields: a Yes/No SCARF flag, and '
       'a monetary threshold, both settable only by the auditors. Transactions posted to a '
       'SCARF account exceeding its threshold are also written to a separate SCARF file, '
       'letting auditors monitor material transactions/sensitive accounts with ease.'],
    ]}},

    {'h4': 'Simulation, program logic/coding, and knowledge-based systems'},
    {'p': '**Simulation** ("parallel simulation") prepares a separate program simulating the '
          'organisation\'s real system — real data is passed through both, e.g. re-performing '
          'controls like identifying missing items from a sequence. **Logical path analysis** '
          'draws flowcharts of program logic; **code comparison programs** compare the '
          'original specified program against the current one, detecting unauthorised '
          'amendments. **Knowledge-based systems** ("decision support" or "expert" systems) '
          'assist the auditor\'s own judgment/decisions, saving time/money by increasing '
          'procedural efficiency, easing record maintenance, reducing required staff numbers, '
          'and letting routine tasks go to technicians assisted by the expert system.'},
  ]},

  {'n': '10.6', 't': 'Controls in a computer environment', 'b': [
    {'key': 'Application and general controls are **inter-related**: strong general controls '
            'add to the assurance obtainable from application controls, while unsatisfactory '
            'general controls can undermine strong application controls, or worsen already-'
            'unsatisfactory ones.'},
    {'p': 'Points influencing the auditor\'s approach: (a) before relying on programmed '
          'application controls, the auditor needs reasonable assurance the programs have '
          'operated properly, via evaluating/testing relevant general controls or other '
          'specific tests; (b) where a programmed procedure lacks effective application '
          'controls, the auditor may test the relevant general controls instead (manually or '
          'via CAATs) to limit substantive procedures; (c) systematic errors can arise from '
          'program faults or hardware malfunction — many should be prevented/detected by '
          'general controls over development, program/data integrity, and operations; and (d) '
          'reliance on general controls may be limited where they lack evidencing or are '
          'applied inconsistently (common with small computers) — in which case the auditor '
          'seeks assurance from manual application-control tests, or specific program-part '
          'tests instead.'},

    {'h4': 'Application controls'},
    {'p': 'Specific requirements to achieve application control objectives: controls over the '
          'completeness/accuracy/authorisation of input; compliance with authorisation '
          'procedures; completeness/accuracy of processing; and maintenance of master files/'
          'standing data files (master files hold permanent information; standing data files '
          'hold current, repeatedly-used information, e.g. staff grades/wage rates).'},
    {'table': {'align': 'll', 'head': ['Application control area', 'Key techniques'], 'rows': [
      ['**Input — completeness**', 'Manual/programmed agreement of control totals; one-for-one '
       'checking of processed output to source documents; sequence checking; programmed '
       'matching against a control file of expected input; and procedures over resubmitting '
       'rejected inputs.'],
      ['**Input — accuracy**', 'Covers both value fields (e.g. invoice amounts) and reference '
       'fields (e.g. account number/date). Techniques: programmed check-digit verification; '
       'programmed reasonableness checks (including logical cross-file relationships); '
       'programmed existence checks against valid codes; and manual output scrutiny.'],
      ['**Authorization**', 'Ensures all transactions are authorised, and by someone empowered '
       'to do so — generally via clerical review (possibly supplemented by a programmed check '
       'for transactions exceeding authorisation limits), done after a control total is '
       'established or after processing, so unauthorised transactions cannot slip in '
       'post-review.'],
      ['**Processing**', 'Ensures all input data is processed; correct master/standing data '
       'files are used; each transaction is processed accurately; new/updated data is accurate '
       'and authorised; and output reports are complete/accurate. The same completeness/'
       'accuracy techniques used for input apply here too, but to the RESULTS of processing '
       '(e.g. a post-update batch reconciliation, not the pre-update one).'],
      ['**Master files and standing data**', 'Similar techniques to transaction input, plus: '
       'more costly one-to-one checking (given these files\' importance); cyclical review of '
       'all master/standing data files; record counts and hash totals used whenever master '
       'files are processed (a check that all records were processed, otherwise of no '
       'significance); and controls over deleting accounts holding a current balance.'],
    ]}},

    {'h4': 'General controls'},
    {'p': 'General controls must: ensure proper development of computer applications; prevent/'
          'detect unauthorised program changes; ensure program changes are adequately tested/'
          'documented; prevent/detect errors during program use; prevent unauthorised data-'
          'file amendments; ensure systems software is properly installed/maintained; ensure '
          'proper documentation is kept; and ensure continuity of operations.'},
    {'table': {'align': 'll', 'head': ['General control area', 'What the auditor considers'],
      'rows': [
      ['**Development of applications**', 'System design standards; programming standards; '
       'documentation controls/standards; testing procedures; approval of development stages '
       'by users and computer management; internal audit involvement; segregation of duties '
       '(design vs. programming vs. operations); and training/supervision.'],
      ['**Preventing/detecting unauthorized program changes**', 'For maintenance: segregation '
       'of duties and staff training/supervision; job authorisation prior to processing; '
       'reviewed change records; password protection; virus checks; emergency modification '
       'procedures; backup-copy integrity; physical protection; offsite extra copies; and '
       'comparison of production programs to controlled copies. For execution: preventing '
       'access to programs while running; controls over utility program use; restricted '
       'computer/terminal access; job-accounting-report review (investigating unusual delays); '
       'and duty rotation.'],
      ['**Testing and documenting program changes**', 'Adequacy of testing procedures; '
       'documentation controls/standards; user and computer-management approval of changes; '
       'internal audit involvement and segregation of duties; and staff training/supervision.'],
      ['**Preventing/detecting execution errors**', 'Adequacy of operations controls in the '
       'systems software; job control procedure libraries; set-up/execution procedures; job '
       'scheduling and emergency backup procedures; and training/supervision — protecting '
       'against incorrect data files, wrong program versions, wrong-sequence running, incorrect '
       'responses to programme requests, and job control errors.'],
      ['**Preventing unauthorized data file amendments**', 'Depends on application controls '
       'over the files, how the file is maintained, and the file management software used. '
       'Considerations: job authorisation prior to processing; unauthorised-amendment '
       'detection; password protection and investigation of unauthorised access attempts; '
       'emergency modification procedures; backup integrity; physical protection; restricted '
       'utility program use; and segregation of duties.'],
      ['**Systems software installation/maintenance**', 'Systems software (operating system, '
       'teleprocessing monitors, database management systems, etc.) needs controls both '
       'exercised BY it and over it: amendment frequency, amendment procedures, access '
       'controls, and segregation of duties.'],
      ['**Proper documentation**', 'Aids efficient/accurate operation, application setup/'
       'amendment, and disaster recovery. Considerations: documentation quality; standards '
       'quality; enforcement of standards and internal audit involvement; updating '
       'procedures.'],
      ['**Continuity of operations**', 'Backup procedures (e.g. off-site extra program copies); '
       'testing of backup facilities/procedures; equipment protection against fire/hazards; '
       'separate power sources; emergency/disaster recovery procedures; and maintenance '
       'agreements/insurance.'],
    ]}},
  ]},

  {'n': '10.7', 't': 'Controls in online and real-time systems', 'b': [
    {'table': {'align': 'll', 'head': ['System', 'Definition'], 'rows': [
      ['**On-line systems**', 'Provide facilities for data to pass to/from the central '
       'computer via remote terminals.'],
      ['**Real-time systems**', 'A further development permitting immediate updating of '
       'computer-held files — input and file-update phases merge, and the system accepts '
       'individual transactions rather than batches. Often called "one-write" systems — the '
       'computerised equivalent of carbon-copy bookkeeping (sales day book, customer account, '
       'customer statement all prepared simultaneously).'],
    ]}},
    {'p': 'Control problems in real-time systems (concerned primarily with larger, multi-user '
          'systems — "terminals" meaning dumb terminals or networked PCs):'},
    {'table': {'align': 'll', 'head': ['Problem', 'Control response'], 'rows': [
      ['**Segregation of duties**', 'The same person often produces and processes the same '
       'information — supervisory controls should be strengthened to compensate for the '
       'reduced internal check.'],
      ['**Data file security**', 'Remote terminal access requires special controls against '
       'accidental/deliberate unauthorised reading, writing or destruction — partly physical '
       '(restricted terminal access, locked terminals/rooms when unused) and partly via the '
       'operating system (passwords/badges/keys, sometimes tiered — one for reading, another '
       'for writing, a third for both; restriction of certain users to certain files; logging '
       'of attempted violations, possibly with automatic shutdown). Application controls can '
       'add validity checks on input and reporting of unusual transactions.'],
      ['**Program security**', 'The same considerations as data file security apply equally to '
       'programs.'],
      ['**Back-ups**', 'Needed at least daily, plus separately weekly. A real-time system may '
       'need a cut-off time after which no further transactions post — since opening a file '
       'during backup can corrupt the process, and stray post-backup transactions could be '
       'lost if a restore is needed. Immediate file access does allow more sophisticated '
       'checks (e.g. extensive computer matching of input against held data), and lets users '
       'immediately correct certain error types, despite the abuse potential.'],
    ]}},

    {'h4': 'Database Management Systems (DBMS)'},
    {'key': 'DBMS are normally designed for real-time environments, letting data elements be '
            'accessed by different programs — avoiding the data duplication that inevitably '
            'occurs in traditional systems. Since data is normally stored **only once** and '
            'accessible to all users needing it, the principal control problems concern '
            '**authorising data amendments** and **restricting access**. An independent '
            'administration function should run day-to-day database operations, enhancing '
            'segregation of duties (independent of systems development, programmers, and the '
            'data processing manager).'},
    {'p': 'DBMS-specific controls: preventing unauthorised program changes (restricted live-'
          'program-file access, password protection, restricted computer/terminal access, '
          'console-log maintenance reviewed by the data processing manager and an independent '
          'party like internal audit, periodic comparison of live programs to control copies); '
          'preventing/detecting operational errors (password-restricted terminal/field access, '
          'satisfactory application controls, operations manuals and user training, logs of '
          'unauthorised access attempts reviewed regularly, physical data protection, '
          'emergency-procedure training); and ensuring database integrity (restricted access '
          'to the data dictionary — the standard descriptions of data definitions/'
          'characteristics/inter-relationships — segregation of duties between the data '
          'processing manager, database administration and systems development, liaison '
          'between database administration and systems development for specification '
          'integrity, and preparation/updating of user manuals alongside the data '
          'dictionary).'},
    {'warn': 'Auditing DBMS creates particular problems, since the two principal CAATs (test '
             'data and audit software) tend to work unsatisfactorily on DBMS programs/files — '
             'auditors may instead use embedded audit facilities, close liaison with internal '
             'auditors, and, ideally, involvement at the evaluation/design/development stages '
             'to identify audit requirements and control problems **before** implementation.'},
  ]},

  {'n': '10.8', 't': 'Business systems and associated IT risks', 'b': [
    {'p': 'Clients relying on IT for key business activities face three main risk categories: '
          'natural disaster, general IT risks, and criminal IT risks.'},
    {'table': {'align': 'll', 'head': ['Category', 'Examples'], 'rows': [
      ['**Natural disasters**', 'Floods, earthquakes, fire — damaging buildings/hardware, '
       'causing loss or corruption of business data records.'],
      ['**General IT threats**', 'Viruses (self-copying, spreading, disruptive programs); '
       'spam/scams/phishing (unsolicited emails fooling people into revealing details or '
       'buying fraudulent goods); malware (malicious disruptive programs); human error '
       '(incorrect processing, careless disposal, opening infected attachments); and hardware/'
       'software failure (power outages, data corruption).'],
      ['**Criminal IT threats**', 'Denial-of-service attacks (preventing authorised website '
       'access); fraud (altering data for illegal benefit); hackers (illegal system '
       'break-ins); password theft (a common hacker tool); security breaches (online '
       'intrusion, physical break-ins); and staff dishonesty (theft of sensitive information, '
       'e.g. customer details).'],
    ]}},
    {'p': 'Main effects of IT risk: loss of confidential/sensitive data; loss of business '
          'continuity; brand/reputational damage; and regulatory fines for negligence.'},
    {'key': 'Preventive measures focus on **business continuity**: identifying/preventing/'
            'reducing risks; insuring against risks that cannot be controlled; and ensuring '
            'quick response/recovery if a risk materialises.'},
    {'p': 'Specific risk-and-inhibition pairs: Trojans (disguised harmful software) — install '
          'anti-virus software; Malware — install anti-virus software, use and regularly '
          'change strong passwords; Spam (bulk unsolicited email) — use inbox junk-email '
          'filters; Cookies (tracking software reporting movements back to the originating '
          'site) — regularly clear browser cookies; Identity theft (using client information '
          'to commit fraud) — store identity information securely and never share it with '
          'untrusted sources; Phishing (fake emails capturing sensitive data) — never open/'
          'click links in unsolicited emails; Hackers — keep software updated, use a '
          'firewall, and create non-disclosure agreements with employees; and Theft of IP/'
          'client data — complete security training with personnel, create security policies/'
          'procedures, and identify/secure valuable data.'},
  ]},

  {'n': '10.9', 't': 'Current trends in information technology', 'b': [
    {'h4': '§10.9.1 Big data analytics'},
    {'def': {'t': 'Big data', 'd': 'a mixture of structured, semi-structured and unstructured '
                  'data collected by organisations, mined for information and used in advanced '
                  'analytics applications (predictive modelling, machine learning).'}},
    {'key': 'Big data is defined by its **three Vs**: **volume** (data comes from many '
            'environments, in large amounts), **variety** (frequently wide-ranging), and '
            '**velocity** (generated/collected/processed at high speed) — datasets so '
            'voluminous that traditional data processing software cannot manage them, yet '
            'valuable because they solve business problems.'},
    {'p': 'Big data helps: improve operational efficiencies; optimise product development; '
          'drive new revenue/growth opportunities; streamline resource management; and enable '
          'smart decision-making. High-performance analytics applied to big data '
          'accomplishes: determining root causes of failures/issues/defects; spotting '
          'anomalies faster/more accurately; swiftly converting data outcomes into insight; '
          'speedily recalculating entire risk portfolios/scenarios; sharpening deep-learning '
          'models\' classification/reaction ability; and detecting fraudulent behaviour before '
          'it affects the organisation.'},

    {'h4': '§10.9.2 Audit of electronic transactions'},
    {'p': 'Electronic commerce has penetrated every facet of human endeavour, with cashless '
          'transactions consummated via digital platforms. The auditor observes four '
          'procedures:'},
    {'table': {'align': 'll', 'head': ['Procedure', 'What it involves'], 'rows': [
      ['**Identify accepted payment methods**', 'Obtain a list of accepted payment types and '
       'process maps for each channel (credit/debit cards, mobile wallets, digital currencies '
       'like Bitcoin, ACH payments, wire transfers, intermediary payments like Interswitch/'
       'PayPal); review how cashless receipts flow into the company\'s bank account; and amend '
       'the audit programme to review them in detail based on how many cashless methods are '
       'used.'],
      ['**Evaluate roles and responsibilities**', 'Obtain a list of employees involved in '
       'receiving/recording/analysing/reporting cashless transactions; review how employee '
       'access to every connected technology platform is managed/monitored; and evaluate who '
       'handles each aspect of the cashless payment cycle, checking security and segregation '
       'of duties is adequate to prevent fraud/misstatement.'],
      ['**Test the reconciliation process**', 'Review prior sales reconciliations for accuracy '
       'and appropriate revenue recognition (especially challenging under new long-term-'
       'contract revenue recognition rules); and test accounting entries for accounts like '
       'inventory, deferred revenue and accounts receivable.'],
      ['**Analyze trends**', 'Cashless transactions create an electronic audit trail, letting '
       'the auditor analyse sales by payment channel over time and by employee/unit, comparing '
       'against prior years to uncover anomalies; and collect information on past payment '
       'problems and the remedial actions taken.'],
    ]}},

    {'h4': '§10.9.3 Artificial Intelligence (AI)'},
    {'def': {'t': 'Artificial Intelligence', 'd': 'the ability of a computer, or a computer-'
                  'controlled robot, to perform tasks normally requiring human intelligence and '
                  'discernment — the simulation of human intelligence in machines programmed to '
                  'think like, and mimic the actions of, humans.'}},
    {'p': 'Examples: conversational bots; email spam filters; Netflix recommendations; robo-'
          'advisors; self-driving cars; and smart assistants (Siri, Alexa).'},
    {'table': {'align': 'lll', 'head': ['Dimension', 'Weak AI', 'Strong AI'], 'rows': [
      ['Application', 'Narrow', 'Wide'],
      ['Scope', 'Limited', 'Vast'],
      ['Good at', 'Specific tasks', 'Human-level intelligence'],
      ['Process', 'Supervised/unsupervised learning', 'Clustering and association'],
    ]}},
    {'note': 'Siri and Alexa are examples of weak AI; advanced robotics represents strong AI. '
             'AI aids human capabilities, simplifying effort and supporting better decisions — '
             'used by companies to improve process efficiency, automate resource-heavy tasks, '
             'and make data-based business predictions.'},
    {'p': 'AI\'s uses in data processing: searching within data and optimising for the most '
          'relevant results; logic-chains for if-then reasoning executing command strings '
          'based on parameters; pattern-detection identifying significant patterns in large '
          'datasets; and applied probabilistic models predicting future outcomes.'},
    {'p': 'Advantages of AI: constant (24-hour) availability; digital assistance; efficient '
          'communication; faster decisions; helps with repetitive work (no fatigue); improves '
          'security (digital surveillance); medical applications (diagnosis, drug dispensary, '
          'advisory); rational, data-based decision-making; and reduction in human error.'},

    {'h4': '§10.9.4 Machine Learning (ML)'},
    {'def': {'t': 'Machine Learning', 'd': 'a form of AI that uses data to teach machines how '
                  'to make inferences and decisions from past experience, rather than through '
                  'explicit programming — recognising patterns and categorising past data to '
                  'infer the meaning of current data and reach a conclusion without human '
                  'assistance.'}},
    {'key': 'ML is both an **art** (reducing disparate problems to a set of acceptable '
            'prototypes) and a **science** (solving those problems and guaranteeing the '
            'recommended solutions) — helping businesses make better decisions, handle larger '
            'volumes, and save man-hours.'},
    {'p': 'Business applications: search-engine webpage ranking; Amazon attracting users to '
          'purchase more books; Netflix inviting additional video rentals; multilingual '
          'automatic translation (e.g. at the UN); speech recognition for verbal approvals; '
          'and face recognition for restricted-premises access.'},
    {'p': 'Types of ML: **Supervised Learning** (humans feed the machine data); **Unsupervised '
          'Learning** (the machine learns on its own, without human assistance); '
          '**Reinforcement Learning** (the machine is rewarded for doing the job as expected); '
          '**Deep Learning** (the human brain is simulated in the machine, so it learns on its '
          'own); and **Deep Reinforcement Learning** (incentivising/rewarding a Deep Learning '
          'network for expected performance).'},
  ]},

  {'n': '10.10', 't': 'Chapter summary', 'b': [
    {'ol': [
      'Computers have several uses in audit administration and management, including linked '
      '(cross-referenced) computerised working papers, statistical sampling, and analytical '
      'procedures.',
      'Auditors may use a number of Computer Assisted Audit Techniques (CAATs), including '
      'audit interrogation software, test data, embedded audit facilities, simulation, '
      'logical path analysis, and code comparison programs.',
      'Application controls should ensure the completeness, accuracy and authorisation of '
      'input; the completeness and accuracy of processing; and proper maintenance of master '
      'files and standing data.',
      'General controls are required to ensure proper application development; prevent/detect '
      'unauthorised program changes; ensure all program changes are adequately tested/'
      'documented; prevent/detect errors during program use; prevent unauthorised amendments '
      'to data files; ensure systems software is properly installed/maintained; ensure proper '
      'documentation is kept; and ensure continuity of operations.',
      'The majority of modern systems are real-time systems, where users have instant, direct '
      'access to data. Important real-time controls are segregation of duties, data file '
      'security, program security, and backups.',
      'Many small computer systems use PCs — the major problems being lack of planning over '
      'acquisition/use, lack of documentary evidence, and lack of security/confidentiality.',
      'Big data analytics, audit of electronic transactions, artificial intelligence and '
      'machine learning are current trends in information technology that impact the way '
      'audit is conducted.',
    ]},
  ]},

  {'n': '10.11', 't': 'Study text questions — multiple-choice and short-answer', 'b': [
    {'p': 'The study text closes the chapter with 10 questions — 5 multiple-choice and 5 '
          'short-answer — reproduced below in full with the official answers, each explained. The '
          'Auditing study text sets **no examination-type questions**; this bank is the whole of '
          'its end-of-chapter material.'
},
    {'eg': {'tag': 'Study text', 't': 'The questions, with the official answers', 'open': True, 'q': [
      {'ol': [
        'The possibility of erasing a large amount of information stored on a magnetic tape would '
        'most likely be reduced by using (A) File protection rings; (B) Check digits; (C) '
        'Completeness check; (D) Conversion verification; (E) Parity check.',
        'Which of the following is **not** an example of CAATs? (A) System control and review '
        'file; (B) Integrated test facilities; (C) Read Only Memory; (D) Snapshot; (E) Mapping.',
        'Computers are useful in audit administration to do the following **EXCEPT** (A) Footing '
        'and cross-footing; (B) Carrying forward numerical data to lead schedules; (C) '
        'Highlighting proposed audit recommendations for audit management review; (D) '
        'Consolidating materials in audit working papers in order to prepare the audit report; '
        '(E) None of the above.',
        'Which of the following computer documentations can assist in obtaining an understanding '
        'of the internal control system? (A) Audit trail; (B) Computer log; (C) Record layout; '
        '(D) System flow chart; (E) Programme code analysis.',
        'The loss of audit trail can be overcome through the following techniques **EXCEPT** (A) '
        'Special print-out; (B) Computer programme; (C) Alteration test; (D) Use of test pack; '
        '(E) By not keeping logs.',
        'Controls over transactions and standing data appertaining to each computer-based '
        'accounting system, and therefore specific to each such application, are known as ………',
        'When transactions can be followed stage by stage through a system to ensure that they '
        'have been processed correctly, there is an audit ………',
        'The audit approach which ignores the procedures that take place within the computer '
        'programs and concentrates solely on the input and corresponding output is called ………',
        'Controls which relate to the environment within which computer-based accounting systems '
        'are developed, maintained and operated, and which are therefore applicable to all '
        'applications, are known as ………',
        'Which of the data processing functions should usually be set up to run and control the '
        'day-to-day operations of the database?',
      ]}],
      'a': [
      {'ol': [
        '**A** — file protection rings. These are a **physical** control that prevents writing to '
        'a tape at all. The others are data-validation controls: they check the accuracy of data '
        'being processed, but do nothing to stop a tape being overwritten.',
        '**C** — Read Only Memory is a **hardware component**, not a computer-assisted audit '
        'technique. The other four are recognised CAATs for auditing **through** the computer.',
        '**E** — "none of the above". The question is asking which task a computer **cannot** '
        'help with, and the answer is that it helps with all four, so there is no exception.',
        '**D** — the system flow chart. It shows the **whole flow of data** through the system '
        'and where the controls sit, which is exactly what is needed to understand the control '
        'system. The others give detail about individual files, records or events rather than the '
        'system as a whole.',
        '**E** — not keeping logs would **destroy** what remains of the trail, not restore it. '
        'The trail is recovered by producing special print-outs, writing audit software, and '
        'using test data.',
        '**Application controls.**',
        '**Trail** (audit trail).',
        '**Auditing "round" the computer** — as distinct from auditing **through** the computer, '
        'which tests the processing itself using CAATs.',
        '**General controls.**',
        '**The administration function** — the database administrator.',
      ]}]}},
  ]},
 ],
 'formulas': [],
 'focus':
   'This chapter has the highest technical-vocabulary density of the subject. Focus first on '
   'the application-controls vs. general-controls distinction (specific-to-one-system vs. '
   'environment-wide) — it structures almost everything else in §10.6. Then know: the "around '
   'the computer" vs. "through the computer" audit-approach distinction and why the former is '
   'now discouraged; the two main CAAT categories (audit software, test data) plus the named '
   'techniques (ITF, SCARF, simulation, logical path analysis, code comparison); and the '
   'six IT systems (TPS/OAS/KMS/MIS/DSS/ESS) as a set worth being able to name and distinguish '
   'at a glance. For the "current trends" section, know the three Vs of big data and the '
   'weak-vs-strong AI distinction — these are new-syllabus content and likely to be tested '
   'directly rather than through scenario application.',
 'errors': [
   'Treating application controls and general controls as interchangeable — application '
   'controls are SPECIFIC to one transaction/standing-data system; general controls apply '
   'across the WHOLE computing environment. They are inter-related but distinct, and weak '
   'general controls can undermine even strong application controls.',
   'Assuming "around the computer" auditing remains an acceptable modern default — the '
   'chapter is explicit that it is now frowned upon, precisely because increasing system '
   'complexity has eroded the paper audit trail it depends on.',
   'Confusing test data (inputting data to see what a system does with it, now declining in '
   'use because of file-corruption risk) with embedded audit facilities like ITF/SCARF (built '
   'permanently into the live system, avoiding that exact problem).',
   'Believing the three Vs of big data are volume, variety and VALUE — the correct third V is '
   'VELOCITY (how fast data is generated/collected/processed), not value.',
   'Assuming DBMS can be audited with the same primary CAATs (test data, audit software) used '
   'elsewhere — the chapter explicitly notes these two standard CAATs tend to work '
   'unsatisfactorily on DBMS programs/files, requiring embedded audit facilities and early '
   'auditor involvement instead.',
 ],
 'quiz': {
  'mcq': [
   {'q': 'The possibility of erasing a large amount of information stored on a magnetic tape '
         'would most likely be reduced using',
    'o': ['File protection rings', 'Check digits', 'Completeness check', 'Conversion '
          'verification', 'Parity check'],
    'a': 0,
    'w': 'File protection rings are a physical mechanism specifically designed to prevent '
    'accidental erasure/overwriting of magnetic tape — the other options address different '
    'concerns (data accuracy, completeness, conversion, transmission error detection).',
    'src': 'Chapter 10.6', 'sec': '10.6'},
   {'q': 'Which of the following is NOT an example of CAATs?',
    'o': ['System control and review file', 'Integrated test facilities', 'Read Only Memory',
          'Snapshot', 'Mapping'],
    'a': 2,
    'w': 'Read Only Memory (ROM) is a hardware storage type, not an audit technique — SCARF and '
    'ITF are both named embedded audit facilities, while snapshot and mapping are recognised '
    'CAAT techniques.',
    'src': 'Chapter 10.5', 'sec': '10.5'},
   {'q': 'Computers are useful in audit administration to do the following EXCEPT',
    'o': ['Footing and cross footing', 'Carry forward of numerical data to lead schedules',
          'Highlight proposed audit recommendations for audit management review', 'Consolidate '
          'materials in audit working papers in order to prepare the audit report', 'None of '
          'the above'],
    'a': 4,
    'w': 'All four listed tasks — footing/cross-footing, carrying forward numeric data, '
    'highlighting recommendations, and consolidating materials for the draft report — are '
    'genuine automated-processing uses the chapter describes, so there is no genuine exception '
    'among them.',
    'src': 'Chapter 10.3', 'sec': '10.3'},
   {'q': 'Which of the following computer documentation can assist in obtaining an '
         'understanding of the internal control system?',
    'o': ['Audit trail', 'Computer log', 'Record layout', 'System flow chart', 'Programme code '
          'analysis'],
    'a': 3,
    'w': 'A system flowchart, like its manual counterpart (Chapter 8), diagrammatically records '
    'how the system and its controls actually operate — the standard documentation tool for '
    'understanding internal control.',
    'src': 'Chapter 10', 'sec': '10.4'},
   {'q': 'The loss of audit trail can be overcome through the following techniques EXCEPT',
    'o': ['Special print out', 'Computer programme', 'Alteration Test', 'Use of Test Pack', 'By '
          'not keeping logs'],
    'a': 4,
    'w': 'Not keeping logs is the opposite of a remedy — it actively worsens audit trail loss, '
    'rather than overcoming it; the other four are genuine techniques for recovering or '
    'substituting for a lost audit trail.',
    'src': 'Chapter 10.4', 'sec': '10.4'},
  ],
  'theory': [
   {'q': 'Distinguish between application controls and general controls in a computer '
         'environment, giving one example of each.',
    'marks': 6,
    'a': [
      {'p': '**Application controls** relate to the transactions and standing data pertaining '
            'to a SPECIFIC computer-based accounting system, ensuring the completeness and '
            'accuracy of records and the validity of entries in that particular application — '
            'e.g. programmed check-digit verification on an input reference number.'},
      {'p': '**General controls** relate to the WHOLE environment in which computerised '
            'accounting systems are developed, maintained and operated, applying across ALL '
            'applications — e.g. password protection restricting access to live program '
            'files.'},
      {'p': 'The two are inter-related: strong general controls enhance the assurance an '
            'auditor can place on application controls, while weak general controls can '
            'undermine otherwise-strong application controls.'},
    ], 'src': 'Chapter 10.4', 'sec': '10.4'},
   {'q': 'Explain the Integrated Test Facility (ITF) and System Control and Review File '
         '(SCARF) as examples of embedded audit facilities.',
    'marks': 6,
    'a': [
      {'p': 'An **Integrated Test Facility (ITF)** creates a fictitious entity (e.g. a '
            'department or customer) within the regular live application. Test transactions '
            'are posted to this fictitious entity alongside genuine transactions, and the '
            'results produced by normal processing are compared against a predetermined '
            'expected outcome. Care must be taken (e.g. reversing journal entries at cut-off) '
            'to ensure the fictitious entity never becomes part of actual financial '
            'reporting.'},
      {'p': 'A **System Control and Review File (SCARF)** flags specific accounts (via an '
            'auditor-set Yes/No field) with a monetary threshold, also set only by the '
            'auditors. Transactions posted to a flagged account above its threshold are '
            'automatically written to a separate SCARF file, letting auditors monitor material '
            'transactions or sensitive accounts continuously and with ease.'},
      {'p': 'Both are embedded permanently within the live accounting system, avoiding the '
            'data-corruption risk that affects standalone test data.'},
    ], 'src': 'Chapter 10.5', 'sec': '10.5'},
  ]},
}
